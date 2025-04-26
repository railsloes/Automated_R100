# Task 2 Function Dependencies

**Focus Area:** Notion Integration Tool

**Key Files/Modules (Proposed):**
*   `src/tools/notion_reader.py` (Main module for the tool)
*   `src/utils/secrets_manager.py` (To fetch Notion API token)
*   `src/config.py` (Potentially for Notion API base URL or defaults)
*   Calling code (e.g., `src/rules/generate_project_definition.py` - hypothetical consumer)

**Call Graph Snippets (Conceptual):**

*   **Initialization:**
    ```mermaid
    graph TD
        A[Consumer Module] --> B(notion_reader.NotionReader.__init__);
        B --> C{utils.secrets_manager.get_secret('NOTION_API_TOKEN')};
        B --> D(notion_client.Client.__init__);
    end
    ```

*   **Reading a Page:**
    ```mermaid
    graph TD
        A[Consumer Module] --> B(notion_reader.NotionReader.get_page_content);
        B -- Page ID --> C(notion_client.Client.blocks.children.list);
        B --> D(Format Notion Blocks to Markdown/JSON);
        C --> E{Handle API Errors/Rate Limits};
        B --> F(Return Formatted Content);
    end
    ```

*   **Reading a Database:**
    ```mermaid
    graph TD
        A[Consumer Module] --> B(notion_reader.NotionReader.get_database_rows);
        B -- Database ID, Filter --> C(notion_client.Client.databases.query);
        B --> D(Process/Format Database Rows);
        C --> E{Handle API Errors/Rate Limits};
        B --> F(Return Processed Rows);
    end
    ```

**Imports/Exports:**
*   `tools/notion_reader.py` will import `notion_client`, `utils.secrets_manager`.
*   Consumer modules will import `tools.notion_reader.NotionReader`.

**External Dependencies:**
*   `notion-client` (Python library - To be added)
*   Potentially `python-dotenv` or similar for local development secrets.
