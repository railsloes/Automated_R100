## **Your Task: Analyze a Project within Radical100 and Generate System Description & Automation Ontology**

You are an AI assistant tasked with analyzing a specific project/feature, described in the provided Product Requirements Document (PRD), within the context of the Radical100 framework (including the `Human-Proxy` team, `Internal Storage`, and the concept of a `State Manager` team). Your goal is to produce two outputs in a single run:

1. **A Detailed Radical100 System Design Document:** A structured report detailing the necessary components (External Interfaces, Event Handling, Teams, Tools, Internal Storage, Containers) for implementing the feature described in the PRD, following the specific instructions in Part 1 below and adhering to Radical100 best practices regarding team responsibility and container orchestration.
2. **A Relational Ontology Mermaid Diagram:** A Mermaid class diagram visualizing the "Automation Entities" involved in the project, derived directly from the system design document (Part 1), following the updated ontology guidelines in Part 2. **Note:** Containers (orchestrators), Events (triggers), Internal Tools (most team-internal helpers), and State Manager teams themselves should *not* appear as distinct entities in this ontology diagram. However, External Human Actors (e.g., Client, User) *should* be included if they interact directly with a `Human-Proxy` team. Data Sources (External Interfaces, Internal Storage) are included *only when actively used*.

**Input:**

1. **Radical100 Framework Technical Description:** (Updated version provided below)
2. **Project Description / PRD:** (Provided below - this specific PRD, e.g., the "Automated Meeting Summary Generator" example, should guide the component definitions in Part 1)

**Core Instructions:**

Use the provided **Project Description / PRD** and the **Radical100 Framework Technical Description** to perform the analysis and generate the outputs.

**Part 1: Generating the Radical100 System Design Document**

**(Based specifically on the PROVIDED PRD below and the Radical100 Framework Technical Description below, define the necessary components for implementing the feature described in the PRD (e.g., "Automated Meeting Summary Generator"). Your output for this part should be a structured design document following the sections below.)**

1. **EXTERNAL INTERFACES & FRONTEND TASKS**
    - **External Frontend (e.g., Retool):** Describe the user interface elements needed (e.g., file upload button, URL input field, submit button) and what information they capture (audio source, user ID). Explain how the submission triggers the workflow (e.g., calls a webhook).
    - **External Services (Notion, Transcription API, Notification API - if used):** For each service:
        - Describe its role in the workflow.
        - Specify any relevant tables, data structures, or API endpoints used (e.g., Notion database ID and schema, transcription API endpoint, Slack channel ID).
        - Note the key information exchanged (e.g., sending audio data, receiving transcript, sending formatted summary, sending notification payload). Note if a service like Slack/Email is handled internally by the `Human-Proxy` Team instead (handling the *mechanics* of sending/receiving).
2. **EVENT HANDLING**
    - Explain how the initial trigger event (e.g., Retool submission via webhook) is received by the framework (e.g., Hookdeck).
    - Clarify the initial parsing: What information is extracted from the incoming event?
    - Which Container or initial task is triggered by this event?
    - Describe any subsequent events (e.g., an event triggering the final notification if not handled directly by a Team like `Human-Proxy`).
3. **INTERNAL STORAGE** (If used)
    - Describe the purpose of the Internal Storage bucket in this workflow.
    - Specify the types of files stored (e.g., intermediate audio files, final reports).
    - Note how files are accessed (e.g., specific URI patterns).
4. **TEAM DEFINITIONS**
    - **Guiding Principle:** Adhere to the principle of **single responsibility**. Each Team should focus on a unique, well-defined task. If a task becomes complex, involves multiple distinct steps (e.g., data retrieval, processing, formatting, decision-making), or covers different logical domains, **split it across multiple specialized Teams**.
    - For each **Team** required (excluding internal framework teams like State Manager unless explicitly customized):
        - **DESCRIPTION:** A concise explanation of the Team's *specific and unique* function (e.g., "Generates Meeting Summary from Transcript", "Extracts Action Items from Text", "Manages Email Communication Channel with Client", "Retrieves File from Internal Storage"). Make it detailed enough for an LLM or system component to understand its precise scope.
        - **INPUT:** Outline the data/parameters required for its specific task (e.g., raw transcript text, user ID to notify, *conceptual instructions or content* for messages, file URI). Specify which Container Variable provides this input.
        - **OUTPUT:** Outline the data returned from its specific task (e.g., formatted summary text, list of action item objects, confirmation of message sent/received, file URI). Explain how this output is used.
        - **INTERNAL TOOLS USED:** List the names of the Internal Tools invoked by this Team during its execution. **Note:** Specialized teams like `Human-Proxy` have built-in capabilities for their core function (messaging mechanics) and require fewer or no external Internal Tools *for that function*. Teams interacting with `Internal Storage` might use specific Internal Tools for file operations.
        - **EXECUTION Flow/Steps:** A step-by-step explanation of how the Team operates *within its narrow scope*. Highlight the rationale.
        - **Human-Proxy Specific Guidance:** When defining `Human-Proxy`, ensure its DESCRIPTION and EXECUTION Flow/Steps focus *exclusively* on managing the communication channel mechanics (e.g., receiving user input via Slack, selecting appropriate channel) and **composing/formatting messages based on conceptual instructions or specific content provided as input by other teams**. It may also maintain basic conversational state (like thread IDs). ***Core automation logic, deciding the core content or purpose of the communication, processing received data beyond simple extraction, or making business decisions must be delegated to other specialized Teams.***
        - **State Manager Awareness:** While defining teams, be aware that a `State Manager` team might be implicitly used internally by the Container (especially `FlowchartExecutor`) to manage flow control based on the defined steps and conditions, but you typically don't need to define the `State Manager` explicitly here unless the PRD requires highly custom state management logic implemented as a distinct team.
5. **CONTAINER TOOL DEFINITIONS**
    - For each **Container Tool** required:
        - **DESCRIPTION:** A concise explanation of what the independent Tool does (e.g., "Formats and Writes Data to Notion", "Downloads Audio from URL", "Uploads Report to Internal Storage").
        - **INPUT:** A schema or outline of the required data/parameters (e.g., Notion DB ID, summary text, action items list, file path, target Internal Storage URI). Specify which Container Variables provide these inputs.
        - **OUTPUT:** A schema or outline of the data returned (e.g., success/failure status, Notion page ID, Internal Storage file URI). Explain the purpose of the output.
        - **EXECUTION Flow/Steps:** A step-by-step explanation of how the Tool operates when executed as a stage, including API calls, data manipulation, interactions with Internal Storage (if any), and any decision logic.
6. **INTERNAL TOOL DEFINITIONS**
    - For each **Internal Tool** required (if any are needed besides those built into Teams like `Human-Proxy`, or for specific storage/API interactions):
        - **DESCRIPTION:** A concise explanation of what the independent Tool does (e.g., "Calls Transcription Service API", "Handles Internal Storage Upload/Download").
        - **INPUT:** A schema or outline of the required data/parameters (e.g., audio file path, API key, source/target file URI).
        - **OUTPUT:** A schema or outline of the data returned (e.g., transcript text, API response status, success/failure flag).
7. **CONTAINER DEFINITIONS**
    - For each **Container** needed (likely one main container):
        - **Specify the Container Type:** (e.g., `FlowchartExecutor`, `MultiStageTeamV2`). Explain why this type is suitable.
        - **List Context Variables:** Define all variables needed to manage state and pass data between steps. For each variable, list:
            - `Name`: (e.g., `audio_source_url`, `transcript_text`, `meeting_summary`, `action_items_list`, `notion_page_id`, `user_id_to_notify`, `internal_storage_report_uri`, `message_content_for_proxy`)
            - `Description`: What the variable represents.
            - `Data Type`: (e.g., string, list[dict], boolean)
            - `Origin`: Where the variable is initially populated (e.g., 'Webhook Input', 'Team Output', 'Container Tool Output', 'Internal Storage interaction').
            - `Purpose`: How the variable is used (e.g., 'Input for Summarization Team', 'Used in Notion Tool', 'Condition for branching', 'Reference to file in Internal Storage', 'Content for Human-Proxy to send').
        - **Define Container Steps:** Detail the sequence of operations. **Crucially, the Container defines the overall workflow logic, orchestrating the sequence, inputs, outputs, and conditional execution of the various Teams and Container Tools involved.** This includes defining the conditions under which the internal `State Manager` (if applicable) would determine the next step.
            - Which Team or Container Tool is executed at each step?
            - What are the specific inputs (Context Variables) for that step?
            - What outputs (Context Variables) does the step update?
            - Under what conditions is each step executed (e.g., step order, branching logic like "if transcription_status == 'success'", error handling)?

**Part 2: Generating the Automation Ontology Mermaid Diagram**

Using the detailed information gathered in Part 1 (the Radical100 System Design Document), create a Mermaid class diagram representing the **Automation Entities** ontology for the project.

**Ontology Guidelines:**

1. **Identify Automation Entities:**
    - Focus on the **active components** that perform automation steps or serve as **active data sources/targets** in the flow. Review the **Teams, Container Tools, External Interfaces, Internal Storage, and potentially External Human Actors** defined or implied in Part 1.
    - **INCLUDE:**
        - **Teams:** As primary actors performing their specific, unique tasks (excluding internal framework teams like `State Manager`).
        - **Container Tools:** As components executing specific actions or transformations in the main flow.
        - **Data Sources (External Interfaces & Internal Storage):** Include `External Interfaces` (e.g., Databases, APIs, specific Sheets/Notion pages) and `Internal Storage` *only if they are actively and directly read from or written to* by a **Team** or **Container Tool** within the described automation flow. The data source container itself (e.g., `CustomerDatabase`, `InternalReportStorage`) is the entity.
        - **External Human Actors (e.g., Client, User, Requestor):** Include `*only if they directly interact (send/receive information) with a Human-Proxy Team*` described in Part 1.
    - **EXCLUDE:**
        - **Containers:** Orchestrators, not drawn.
        - **Events:** Triggers, not drawn.
        - **Internal Tools:** Implementation details of Teams. Referenced in relationship labels (Guideline 3).
        - **State Manager Team:** Considered internal framework orchestration logic, not drawn.
        - ***Data Sources used only for triggering:*** E.g., a simple webhook endpoint or email inbox that only starts a container but isn't otherwise directly read/written by Teams/Tools in the flow.
        - **Passive Business Entities:** Background concepts not directly read/written in this specific flow.
    - **Decision Rule:** "Is this element a **Team** (excluding State Manager) or a **Container Tool** defined in Part 1? OR Is it an **External Interface** or **Internal Storage** directly providing input data to, or receiving output data from, a **Team** or **Container Tool**? OR Is it an **External Human Actor** directly interacting with a **Human-Proxy** team?" If YES, include it as a class. Otherwise, EXCLUDE it.
2. **Define Attributes:**
    - For each Automation Entity class (**Team, Container Tool, active External Interface, Internal Storage, External Human Actor**) in the diagram, include relevant attributes focusing on:
        - `Primary Identifiers`: Unique IDs or names (e.g., `TeamName`, `ContainerToolName`, `DatabaseURL`, `APIEndpoint`, `StorageName`, `UserID`, `ClientEmail`).
        - `Data Source Location/Access Attributes`: For Data Source entities (`External Interface`, `Internal Storage`), attributes specifying location and access (e.g., `FilePath`, `APIEndpoint`, `BaseURI`, `SheetID`).
        - `Data Source Keys/References`: Attributes acting as keys or references *if* the entity links to specific records within *another* data source.
        - `Automation State Attributes`: Capture status relevant to the flow (e.g., `TaskStatus` on a Team, `InteractionChannel` or `ConversationStatus` for `Human-Proxy`, `LastAccessed` for storage).
        - `Relevant Data Fields`: Use *very sparingly*. Include only if essential for understanding the entity's role in a key interaction (e.g., `ClientEmail` on `Client` if used directly by `Human-Proxy`).
    - **Derive these attributes directly from the details provided in Part 1.**
3. **Define Relationships:**
    - Draw relationships **between the identified Automation Entity classes (Teams, Container Tools, active Interfaces, Internal Storage, relevant Human Actors)** reflecting the interactions orchestrated by the Containers, as described in the **Execution Flows** and **Container Steps** from Part 1.
    - Use **Descriptive Labels** for relationships. Examples: `invokes`, `uses` (for Container Tools), `reads from`, `writes to`, `updates`, `generates`, `sends data to`, `receives data from`, `provides input to`, `gets output from`, `queries`, `stores file in`, `retrieves file from`, `sends email to`, `receives Slack message from`.
    - **Representing Internal Tool Usage:** If a **Team** uses an **Internal Tool** to interact with another modeled entity, **incorporate the Internal Tool's name into the relationship label**. Format: `TeamA --> TargetEntity : "uses InternalToolName to [action]"` (e.g., `"uses StorageHandlerTool to store file in"`).
    - **Representing Human-Proxy Interactions:** Relationships involving `Human-Proxy` should reflect *communication actions only* (sending/receiving messages). Labels should be like `sends email to`, `receives Slack message from`, `requests input via Teams`. These labels represent the communication act; the *content* being communicated is typically determined by another team providing input to `Human-Proxy` (often via container variables). Relationships representing the *processing* of received data or the *generation* of content to be sent should originate from *other* Teams that perform those logic tasks.
    - **Representing Event Triggers:** If a Team or Container Tool's execution is initiated by an event from an *included* External Interface entity, you might use labels like `initiated by event from` or `reacts to event from`.
    - **`Ensure these relationship labels and connections directly mirror the interactions between the included entities, as dictated by the EXECUTION Flow/Steps (for Teams/Tools) and Execution Steps/Logic (for Containers) documented in Part 1, incorporating Internal Tool names in labels where appropriate, and correctly modeling Human-Proxy communication-only interactions and Internal Storage access.`**
    - Show clear data flow and control flow between the included entities.
    
    ```
    /* Illustrative Snippet:
       If Part 1 defines:
       - 'ContentGenTeam' generates report text.
       - 'HumanProxyTeam' sends the report text (received as input) via email to 'Client'.
       - 'Client' sends feedback via Slack to 'HumanProxyTeam'.
       - 'FeedbackProcessingTeam' receives feedback text from HumanProxyTeam (via context variable).
       The Mermaid ontology might include:
    */
    class ContentGenTeam {
      +TeamName
    }
    class HumanProxyTeam {
      +TeamName
      +ManagedChannels
    }
    class Client {
      +ClientID
      +ClientEmail
      +ClientSlackID
    }
    class FeedbackProcessingTeam {
        +TeamName
    }
    
    // ContentGenTeam --> (Output passed via Container Variable, not direct link shown here)
    HumanProxyTeam --> Client : "sends email to"
    Client --> HumanProxyTeam : "sends Slack message to"
    // HumanProxyTeam --> (Feedback passed via Container Variable to FeedbackProcessingTeam)
    // Note: Direct links show interaction between modeled entities. Data passing via container variables between steps isn't always a direct arrow unless one entity invokes the next. Container logic defines the sequence.
    
    ```
    
4. **Conceptual Iteration (Internal Process):**
    - As you define the elements in Part 1, mentally map the **Teams, Container Tools, actively participating External Interfaces, Internal Storage, and External Human Actors (interacting via Human-Proxy)** to potential Automation Entities.
    - While detailing Execution Flows and Container Steps (Part 1), mentally refine the entities, attributes, and relationships (including Internal Tool references, Human-Proxy communication-only interactions, and Internal Storage interactions) in your conceptual ontology.

**Final Output Requirements:**

Provide your response as a single block containing:

1. The complete, structured **Radical100 System Design Document** (following the format in Part 1 above, based on the specific PRD provided).
2. Immediately following the report, the complete **Mermaid Class Diagram** code block (`mermaid ...` ) representing the final, refined Automation Entity ontology derived from the report. DO NOT include any comment in the code.
3. **Consistency Check:** Before finalizing, ensure that every major **active component (Team [excl. State Manager], Container Tool, active Interface, Internal Storage, relevant External Human Actor)** described in the Part 1 report has a corresponding class in the Part 2 Mermaid diagram, and that the relationships visually reflect the interactions documented in the report, respecting the single responsibility principle for Teams.

**(Radical100 Framework Technical Description - Updated)**

1. **External Interfaces**
    - **External Frontend:** Provides custom configurations for services like Notion, Spreadsheets, Retool, etc.
    - **Events:** Receives events from external applications via a designated webhook or through Hookdeck. Events are parsed and redirected to the appropriate internal task.
2. **Containers**
    - Orchestrate multi-stage tasks, managing context (variables) and state across stages. **Define the workflow logic, sequence, and conditions for executing Teams and Tools.**
    - **Types:** `MultiStageTeamV2`, `FlowchartExecutor`.
3. **Teams**
    - Groups of agents (LLMs) executing specific, unique tasks, potentially invoking Internal Tools. Use container variables for Input/Output. **Best Practice:** Teams should have a single, well-defined responsibility. Complex processes should be split across multiple teams.
    - **Team Types:**
        - `LiteLLMTeamV2`: General LLM interaction.
        - `AutogenAssistantTeam`: Single agent with tool execution via Internal Tools.
        - `AutogenGroupchatTeam`: Multi-agent collaboration.
        - `OpenAIAssistant`: OpenAI Assistant API wrapper.
        - `LlamaIndexWorkflow`: LlamaIndex task management.
        - **`Human-Proxy`**: Manages the *mechanics* of user interaction (sending/receiving via Email, Slack, Teams etc.), **composes messages based on conceptual instructions or content provided by other teams**, and handles basic conversation flow. **Does not perform core automation logic, content generation (beyond formatting based on input), or decision-making**; these tasks belong to other teams. Reduces need for messaging Internal Tools *for communication tasks*.
        - `Special Task Management Teams`: MapReduce, BatchExecutor.
        - **`State Manager`**: (Internal Framework Team) Decides the next step in a workflow based on current state and predefined logic defined within the Container. Often used implicitly by complex Containers like `FlowchartExecutor`. **Note:** Generally *not* modeled as a distinct entity in the Automation Ontology (Part 2).
4. **Container Tools**
    - Scripts empowering Containers, executed as stages. Use container variables for Input/Output. Used for external calls, data distribution, complex coded operations outside of Teams.
5. **Internal Tools**
    - Scripts empowering Teams (except where built-in capabilities exist, e.g., `Human-Proxy` messaging). Use Team-internal data for Input/Output. Used for API calls, complex computations within a Team's task.
6. **Internal Storage**
    - A managed file storage service (bucket) accessible by Teams and Container Tools within the framework via unique URIs. Used for storing/retrieving intermediate or final file-based artifacts.
7. **Project Structure and Task Management**
    - Tasks classified as: External Frontend, Events, Tools (Internal/Container), Teams, Internal Storage interaction, or Containers.
    - All major components require: Input/Output schema (where applicable), clear description, execution steps (where applicable).

**(Now, provide the specific Project Description / PRD below this line when you use this prompt)**

`[PROJECT DESCRIPTION / PRD WILL BE PROVIDED HERE]`