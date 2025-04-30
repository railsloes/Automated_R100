# Google Slides Translator

This project provides a script to translate Google Slides presentations using the ChatGPT API. The script takes a Google Slides presentation ID and a target language, translates the text content, and generates a new presentation with the translated text.

## Features

- Authenticates with Google APIs using OAuth 2.0
- Creates a copy of the original presentation
- Extracts all text content from slides
- Translates text using OpenAI's ChatGPT API
- Replaces text in the copied presentation with translations
- Returns the ID of the newly created, translated presentation

## Prerequisites

- Python 3.6+
- Google Cloud Project with Slides and Drive APIs enabled
- OAuth 2.0 credentials (credentials.json file)
- OpenAI API key

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Google Cloud Project:
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Google Slides API and Google Drive API
   - Create OAuth 2.0 credentials (Desktop app) and download as `credentials.json`
   - Place the `credentials.json` file in the project root directory

4. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key'
```

## Usage

Run the script from the command line:

```bash
python slides_translator.py --presentation-id "YOUR_PRESENTATION_ID" --target-language "Spanish"
```

### Parameters

- `--presentation-id`: The ID of the Google Slides presentation to translate (required)
- `--target-language`: The target language for translation (e.g., "Spanish", "French", "German") (required)

### How to find your presentation ID

The presentation ID is the string of characters in the URL of your Google Slides presentation:
```
https://docs.google.com/presentation/d/YOUR_PRESENTATION_ID/edit
```

## Example

```bash
python slides_translator.py --presentation-id "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms" --target-language "French"
```

## First-time Authentication

The first time you run the script, it will open a browser window asking you to authorize the application to access your Google Slides and Drive. After authorization, the script will save a `token.json` file for future use.

## Notes

- The script processes text replacements in batches to avoid exceeding API limits
- If a translation fails, the original text will be preserved
- The script provides progress updates during execution
