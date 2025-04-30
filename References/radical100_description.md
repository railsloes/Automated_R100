You are an engineering manager working to integrate a new feature within the Radical100 framework.

**PROVIDED Product Requirements Document (PRD): SAMPLE**

---

**YOUR TASK**

Based *specifically* on the **PROVIDED PRD** above and the **Radical100 Framework Technical Description** (provided below), define the necessary components for implementing this "Automated Meeting Summary Generator" feature. Your output should be a structured design document.

**Define External Interfaces & Frontend Tasks:**

- **External Frontend (e.g., Retool):** Describe the user interface elements needed (e.g., file upload button, URL input field, submit button) and what information they capture (audio source, user ID). Explain how the submission triggers the workflow (e.g., calls a webhook).
- **External Services (Notion, Transcription API, Notification API - if used):** For each service:
    - Describe its role in the workflow.
    - Specify any relevant tables, data structures, or API endpoints used (e.g., Notion database ID and schema, transcription API endpoint, Slack channel ID).
    - Note the key information exchanged (e.g., sending audio data, receiving transcript, sending formatted summary, sending notification payload). *Note if a service like Slack/Email is handled internally by the Human-Proxy Team instead.*

**Define Event Handling:**

- Explain how the initial trigger event (e.g., Retool submission via webhook) is received by the framework (e.g., Hookdeck).
- Clarify the initial parsing: What information is extracted from the incoming event?
- Which Container or initial task is triggered by this event?
- Describe any subsequent events (e.g., an event triggering the final notification if not handled directly by a Team like Human-Proxy).

**Define the Teams required:** For each Team, include:

- **DESCRIPTION:** A concise explanation of the Team's specific function (e.g., "Generates Meeting Summary", "Extracts Action Items", "Handles User Notification"). Make it detailed enough for an LLM or system component to understand *when* and *why* to invoke it.
- **INPUT:** Outline the data/parameters required (e.g., raw transcript text, user ID to notify, message content). Specify which Container Variable provides this input.
- **OUTPUT:** Outline the data returned (e.g., formatted summary text, list of action item objects, notification confirmation). Explain how this output is used (e.g., stored in a Container Variable, confirms completion).
- **INTERNAL TOOLS USED:** List the *names* of the Internal Tools invoked by this Team during its execution (e.g., `llm_api_call_tool`). *Note: Specialized teams like Human-Proxy may have built-in capabilities and require fewer or no external Internal Tools for core functions like messaging.*
- **EXECUTION Flow/Steps:** A step-by-step explanation of how the Team operates once invoked, including interactions with Internal Tools (if any) and any internal decision logic. Highlight the rationale.
- ***Guidance:** Consider if specialized Teams described in the framework (see Section 3 below), like `Human-Proxy` for user interactions/notifications or task management teams, are suitable for any required step based on the PRD.*

**Define the Container Tools required:** For each Container Tool, include:

- **DESCRIPTION:** A concise explanation of what the independent Tool does (e.g., "Formats and Writes Data to Notion", "Downloads Audio from URL"). Make it detailed enough for understanding *when* and *why* it's invoked within a Container's stage.
- **INPUT:** A schema or outline of the required data/parameters (e.g., Notion DB ID, summary text, action items list). Specify which Container Variables provide these inputs.
- **OUTPUT:** A schema or outline of the data returned (e.g., success/failure status, Notion page ID). Explain the purpose of the output (e.g., confirm successful storage, update a status variable).
- **EXECUTION Flow/Steps:** A step-by-step explanation of how the Tool operates when executed as a stage, including API calls, data manipulation, and any decision logic. Highlight the rationale.

**Define the Internal Tools required:** For each Internal Tool (if any are needed besides those built into Teams like Human-Proxy), include:

- **DESCRIPTION:** A concise explanation of what the independent Tool does (e.g., "Calls Transcription Service API"). Make it detailed enough for a Team Agent to understand its function.
- **INPUT:** A schema or outline of the required data/parameters (e.g., audio file path, API key).
- **OUTPUT:** A schema or outline of the data returned (e.g., transcript text, API response status).
- *(Note: Execution flow for Internal Tools is often simple script logic, invoked directly by a Team Agent based on its inputs and instructions).*

**Identify and Define Containers relevant to the feature:** For *each* Container needed (likely one main container for the core workflow), you must:

- **Specify the Container Type:** (e.g., FlowchartExecutor, MultiStageTeamV2). Explain *why* this type is suitable for orchestrating the feature's workflow.
- **List Context Variables:** Define all variables needed to manage state and pass data between steps within the container. For each variable, list:
    - `Name:` (e.g., `audio_source_url`, `transcript_text`, `meeting_summary`, `action_items_list`, `notion_page_id`, `user_id_to_notify`)
    - `Description:` What the variable represents.
    - `Data Type:` (e.g., string, list[dict], boolean)
    - `Origin:` Where the variable is initially populated (e.g., 'Webhook Input', 'Team Output', 'Container Tool Output').
    - `Purpose:` How the variable is used (e.g., 'Input for Summarization Team', 'Used in Notion Tool', 'Condition for branching').
    - *(Reminder: These are variables for orchestrating Container steps, not variables used only internally within a single Team's execution).*
- **Define Container Steps:** Detail the sequence of operations:
    - Which Team or Container Tool is executed at each step?
    - What are the specific inputs (Context Variables) for that step?
    - What outputs (Context Variables) does the step update?
    - Under what conditions is each step executed (e.g., step order, branching logic like "if `transcription_status == 'success'`", error handling)?

---

**WHAT THE FINAL “REPORT” SHOULD LOOK LIKE**

Structure the final report using the component definitions requested above:

1. EXTERNAL INTERFACES & FRONTEND TASKS
2. EVENT HANDLING
3. TEAM DEFINITIONS
4. CONTAINER TOOL DEFINITIONS
5. INTERNAL TOOL DEFINITIONS
6. CONTAINER DEFINITIONS

Ensure each section includes all the specified details (Description, Input, Output, Execution Flow, Variables, etc., as applicable per the instructions above).

---

**ADDITIONAL NOTES & RECOMMENDATIONS**

- Refer to the Radical100 framework sections below for detailed definitions of component types.
- Focus on clearly showing how variables and step outputs/inputs link the Teams and Tools together within the Container.
- Highlight any branching conditions or dependencies clearly in the Container steps (e.g., “If `audio_download_successful` = True, proceed to transcription…”).
- Ensure descriptions for Teams, Tools, and Containers are precise enough to allow an orchestrator (like another LLM or system component) to understand their purpose and decide when to invoke them.

---

**The Radical100 Framework Technical Description:**

1. **External Interfaces**
    - **External Frontend:** Provides custom configurations for services like Notion, Spreadsheets, Retool, etc.
    - **Events:** Receives events from external applications via a designated webhook or through Hookdeck. Events are parsed and redirected to the appropriate internal task, typically initiated by the external frontend to interact with tools, teams, or containers.
2. **Containers**
    - Orchestrate multi-stage tasks, managing context and state across different stages, coordinating between teams and tools.
    - **General Characteristics:** Share context information (variables) across stages. Clear functional description. Define conditions for next steps.
    - **Types:** `MultiStageTeamV2` (defined dependencies, stages are Team/Tool), `FlowchartExecutor` (flowchart logic, loops, conditionals).
3. **Teams**
    - Groups of agents (or LLMs) executing specific tasks, potentially invoking Internal Tools.
    - Receive Inputs from container variables.
    - Generate Outputs to update container variables (for subsequent steps or flow control).
    - **General Attributes:** Execute LLMs, configurable, can integrate APIs via Internal Tools.
    - **Team Types:**
        - `LiteLLMTeamV2`: Utilizes LiteLLM to interact with a broad range of models. Ideal for text redaction, structured data extraction, etc.
        - `AutogenAssistantTeam`: Features a single LLM agent capable of tool execution. Best suited for tasks requiring third-party API access or complex computations via Internal Tools.
        - `AutogenGroupchatTeam`: Combines multiple agents with varied roles for collaborative problem-solving.
        - `OpenAIAssistant`: A wrapper around the OpenAI Assistant API, enabling tool execution and integration of OpenAI resources.
        - `LlamaIndexWorkflow`: Manages sequential tasks via LlamaIndex Workflows.
        - `Human-Proxy`: **(New)** Specialized team designed to manage interactions with human users. It has internal capabilities to send/receive messages via channels like Email, Slack, Microsoft Teams, etc., and can maintain conversational context. Often reduces the need for separate Internal Tools for basic messaging tasks.
        - Special Task Management Teams: Includes teams like “MapReduce” and “BatchExecutor,” focusing on task management, data indexing, and retrieval.
4. **Container Tools**
    - Scripts empowering Containers.
    - Receive Inputs from container variables.
    - Generate Outputs to update container variables.
    - Used for: Receiving external context (APIs), distributing results (frontends, DBs), complex coded operations.
    - Defined as a stage within a Container's workflow and use Container variables.
5. **Internal Tools**
    - Scripts empowering Teams (except those with built-in capabilities like Human-Proxy for certain tasks).
    - Receive Inputs *from the Team* during its execution.
    - Generate Outputs that are sent back *to the Team's internal process/conversation*.
    - Used for: Receiving external context (APIs), distributing results, complex coded operations *within* a Team's task.
    - *Not* defined directly in the Container workflow or variables; used *by* agents within Teams.
6. **Project Structure and Task Management**
    - Tasks classified as: External Frontend, Events, Tools (Internal/Container), Teams, or Containers.
    - All Containers, Teams, and Tools require: Input/Output schema, clear description, execution steps (where applicable).