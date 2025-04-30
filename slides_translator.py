#!/usr/bin/env python3
"""
Google Slides Translator

This script takes a Google Slides presentation ID and a target language,
translates the text content using ChatGPT, and generates a new presentation
with the translated text.

Author: Automated_R100
"""

import os
import json
import time
from typing import Dict, Set, List, Optional, Tuple

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from openai import OpenAI

# Define the scopes required for Google APIs
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive']

def get_google_credentials() -> Credentials:
    """
    Handles Google OAuth2 authentication flow.
    
    Args:
        None
        
    Returns:
        Credentials: Google API credentials object
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If credentials don't exist or are invalid, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def create_service_clients(creds: Credentials) -> Tuple:
    """
    Creates Google API service clients.
    
    Args:
        creds: Google API credentials
        
    Returns:
        Tuple: (slides_service, drive_service)
    """
    slides_service = build('slides', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    return slides_service, drive_service

def duplicate_presentation(drive_service, original_presentation_id: str, target_language: str) -> str:
    """
    Creates a copy of the original presentation.
    
    Args:
        drive_service: Google Drive API service
        original_presentation_id: ID of the original presentation
        target_language: Target language for translation
        
    Returns:
        str: ID of the newly created presentation copy
    """
    print(f"Creating a copy of presentation {original_presentation_id}...")
    copy_title = f'Translated - {original_presentation_id} - {target_language}'
    body = {'name': copy_title}
    
    copied_file = drive_service.files().copy(
        fileId=original_presentation_id,
        body=body,
        fields='id'  # Only request the ID field
    ).execute()
    
    translated_presentation_id = copied_file.get('id')
    print(f"Created copy with ID: {translated_presentation_id}")
    return translated_presentation_id

def extract_text_from_presentation(slides_service, presentation_id: str) -> Set[str]:
    """
    Extracts all text content from a Google Slides presentation.
    
    Args:
        slides_service: Google Slides API service
        presentation_id: ID of the presentation
        
    Returns:
        Set[str]: Set of unique text strings found in the presentation
    """
    print("Extracting text from presentation...")
    presentation = slides_service.presentations().get(
        presentationId=presentation_id
    ).execute()

    texts_to_translate = set()  # Use a set to automatically handle duplicates

    if 'slides' in presentation:
        for slide in presentation['slides']:
            if 'pageElements' in slide:
                for element in slide['pageElements']:
                    if element.get('shape') and element['shape'].get('text'):
                        full_text_in_shape = ""
                        text_elements = element['shape']['text'].get('textElements', [])
                        for text_element in text_elements:
                            if text_element.get('textRun') and text_element['textRun'].get('content'):
                                full_text_in_shape += text_element['textRun']['content']
                        cleaned_text = full_text_in_shape.strip()
                        if cleaned_text:  # Add only non-empty, stripped text
                            texts_to_translate.add(cleaned_text)

    print(f"Found {len(texts_to_translate)} unique text strings to translate.")
    return texts_to_translate

def translate_text_with_chatgpt(texts_to_translate: Set[str], target_language: str) -> Dict[str, str]:
    """
    Translates text using the ChatGPT API.
    
    Args:
        texts_to_translate: Set of text strings to translate
        target_language: Target language for translation
        
    Returns:
        Dict[str, str]: Dictionary mapping original text to translated text
    """
    print(f"Translating {len(texts_to_translate)} text strings to {target_language}...")
    
    # Initialize OpenAI client (requires OPENAI_API_KEY environment variable)
    client = OpenAI()
    
    translation_map = {}
    for text in texts_to_translate:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Or another model
                messages=[
                    {"role": "system", "content": f"You are a translation assistant. Translate the following text to {target_language}. Respond ONLY with the translated text, without any introductory phrases or explanations."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3,  # Lower temperature for more deterministic translation
                max_tokens=len(text) * 2 + 50  # Estimate max token need
            )
            translated_text = response.choices[0].message.content.strip()
            # Basic cleaning: Remove potential quotes added by the AI
            if translated_text.startswith('"') and translated_text.endswith('"'):
                translated_text = translated_text[1:-1]
            translation_map[text] = translated_text
            print(f"Translated: '{text[:30]}...' -> '{translated_text[:30]}...'")
            # Add a small delay to avoid rate limits
            time.sleep(0.5)
        except Exception as e:
            print(f"Error translating '{text[:30]}...': {e}")
            translation_map[text] = text  # Keep original if translation fails
    
    return translation_map

def replace_text_in_presentation(slides_service, presentation_id: str, translation_map: Dict[str, str]) -> None:
    """
    Replaces text in the presentation with translated text.
    
    Args:
        slides_service: Google Slides API service
        presentation_id: ID of the presentation
        translation_map: Dictionary mapping original text to translated text
        
    Returns:
        None
    """
    print("Replacing text in presentation with translations...")
    requests = []
    for original, translated in translation_map.items():
        if original != translated:  # Only create requests if translation is different
            requests.append({
                'replaceAllText': {
                    'containsText': {
                        'text': original,
                        'matchCase': True  # Usually best for direct replacement
                    },
                    'replaceText': translated,
                }
            })

    if requests:
        # Process requests in batches to avoid exceeding API limits
        batch_size = 100  # Google Slides API has a limit on batch size
        for i in range(0, len(requests), batch_size):
            batch_requests = requests[i:i+batch_size]
            body = {'requests': batch_requests}
            response = slides_service.presentations().batchUpdate(
                presentationId=presentation_id,
                body=body
            ).execute()
            print(f"Executed batch {i//batch_size + 1}/{(len(requests) + batch_size - 1)//batch_size}: "
                  f"{len(response.get('replies', []))} replacement operations.")
    else:
        print("No text replacements needed.")

def translate_slides_presentation(original_presentation_id: str, target_language: str) -> str:
    """
    Main function to translate a Google Slides presentation.
    
    Args:
        original_presentation_id: ID of the original presentation
        target_language: Target language for translation
        
    Returns:
        str: ID of the translated presentation
    """
    # Authenticate and create service clients
    creds = get_google_credentials()
    slides_service, drive_service = create_service_clients(creds)
    
    # Create a copy of the original presentation
    translated_presentation_id = duplicate_presentation(drive_service, original_presentation_id, target_language)
    
    # Extract text from the original presentation
    texts_to_translate = extract_text_from_presentation(slides_service, original_presentation_id)
    
    # Translate the extracted text
    translation_map = translate_text_with_chatgpt(texts_to_translate, target_language)
    
    # Replace text in the copied presentation
    replace_text_in_presentation(slides_service, translated_presentation_id, translation_map)
    
    print(f"Translation complete! New presentation ID: {translated_presentation_id}")
    return translated_presentation_id

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate Google Slides presentation using ChatGPT')
    parser.add_argument('--presentation-id', required=True, help='ID of the Google Slides presentation to translate')
    parser.add_argument('--target-language', required=True, help='Target language for translation (e.g., Spanish, French)')
    
    args = parser.parse_args()
    
    # Set OpenAI API key from environment variable
    if not os.environ.get('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it with: export OPENAI_API_KEY='your-api-key'")
        exit(1)
    
    # Translate the presentation
    translated_id = translate_slides_presentation(args.presentation_id, args.target_language)
    print(f"\nTranslated presentation ID: {translated_id}")
    print(f"View it at: https://docs.google.com/presentation/d/{translated_id}")
