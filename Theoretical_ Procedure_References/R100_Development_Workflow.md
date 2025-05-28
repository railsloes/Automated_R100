# AI IDE PLAN

## **1. File Structure**

This structure organizes system-level knowledge, project-specific details, sprint management, and task definitions, facilitating navigation and state management for the AI agent.

`├── System_Memory_Bank/             # General Radical100 framework docs & patterns
│   ├── Teams.md                    # Schemas, patterns, test guidelines for Teams
│   ├── Tools.md                    # Schemas, patterns, test guidelines for Tools (Container & Internal)
│   ├── Events.md                   # Schemas, patterns, guidelines for Events
│   ├── Containers.md               # Schemas, patterns, guidelines for Containers
│   ├── deployment_pattern.md       # Standard deployment procedures/checklists
│   ├── testing_definition.md       # General testing strategies & standards
│   ├── Debugging.md                # Common debugging steps & patterns
│   ├── replanning.md               # Guidelines for triggering and executing replanning
│   └── ...                         # Other reusable patterns, style guides, etc.
│
├── Project_Name/                   # Root directory for a specific project
│   ├── src/                        # Source code generated/managed by the agent
│   │   ├── teams/
│   │   ├── tools/
│   │   │   ├── container_tools/
│   │   │   └── internal_tools/
│   │   ├── containers/
│   │   ├── events/
│   │   ├── tests/                  # Test code (e.g., pytest files)
│   │   └── ...                     # Other project-specific code modules
│   │
│   ├── sprints.json                # Summary list of all sprints and their status
│   ├── activeContext.md            # Dynamic state: current focus, recent changes, next steps
│   ├── project_prd.md              # Project Requirements Document
│   ├── project_ontology.md         # Key concepts, entities, and relationships specific to the project
│   ├── automation_entities_summary.md # High-level overview of planned Teams, Tools, Containers, Events (I/O/D)
│   ├── automation_entities.md      # Detailed specification for each planned entity
│   ├── state_manager_instructions.md # Project-specific rules for state variable handling
│   ├── definition_of_done_checklist.md # Project-specific Definition of Done checklist
│   │
│   ├── Sprint_1/                   # Directory for Sprint 1 deliverables and definitions
│   │   ├── tasks.json              # Summary list of tasks for this sprint (status, dependencies)
│   │   ├── tests.json              # Summary list of tests for this sprint (status, dependencies)
│   │   ├── sprint_description.md   # Sprint goals, requirements, scope, DoD, working directory
│   │   │
│   │   ├── Tasks/                  # Detailed task descriptions for the sprint
│   │   │   ├── Task_1.md           # Description, Acceptance Criteria, Reqs, I/O/D, Steps for Task 1
│   │   │   └── Task_2.md           # ...
│   │   │
│   │   └── Tests/                  # Detailed test descriptions for the sprint
│   │       ├── Task_1_Test_1.md    # Description, Use Cases for Test 1 of Task 1
│   │       ├── Task_1_Test_2.md    # ...
│   │       └── Task_2_Test_1.md    # ...
│   │
│   ├── Sprint_2/                   # Directory for Sprint 2
│   │   └── ...                     # (Structure mirrors Sprint_1)
│   │
│   └── auxiliary/                  # Non-essential generated files, logs, etc.
│       ├── generated_data/         # Sample datasets for testing/DoD
│       └── logs/                   # Execution logs
│
└── ...                             # Other Projects`

## **2. Development Workflow Description**

This describes the flow of activities within the agentic IDE, leveraging the file structure and AI capabilities. The AI agent performs most steps, guided by the files and potentially human input/confirmation.

1. **Project Initialization & PRD Creation:**
    - **Trigger:** Human developer initiates a new project.
    - **Action (Human/AI):** Developer provides initial requirements, potentially through interviews/conversations managed by the AI agent. The agent assists in structuring and writing the `project_prd.md`.
    - **File I/O:** CREATE `Project_Name/project_prd.md`.
2. **Global Project Definition Generation:**
    - **Trigger:** Completion of `project_prd.md`.
    - **Action (AI Agent):**
        - Reads `Project_Name/project_prd.md`.
        - Reads relevant guidelines from `System_Memory_Bank/` (e.g., how to define ontologies, entities).
        - Reads `_human structure definition_` (if provided as a separate file or instruction).
        - Generates the initial definitions for the project's core components and structure.
    - **File I/O:**
        - READ: `project_prd.md`, `System_Memory_Bank/*`, `_human structure definition_`.
        - CREATE/WRITE: `project_ontology.md`, `automation_entities_summary.md`, `automation_entities.md`, `state_manager_instructions.md`, `definition_of_done_checklist.md`.
        - UPDATE: `activeContext.md` (reflecting completion of this stage, next step is planning).
3. **Project Planning (Sprint Generation):**
    - **Trigger:** Completion of Global Project Definition.
    - **Action (AI Agent):**
        - Reads the generated definition files (`project_prd.md`, `automation_entities.md`, `definition_of_done_checklist.md`, `state_manager_instructions.md`, `project_ontology.md`).
        - Consults `System_Memory_Bank/` for planning patterns.
        - Optionally queries the "host assistant" (or a vector DB) to identify existing reusable Teams/Tools based on descriptions in `automation_entities.md`. Incorporates developer instructions regarding reuse.
        - Breaks down the project into logical Sprints based on dependencies outlined in `automation_entities.md`.
        - Generates the overall sprint plan and the description for the first sprint.
    - **File I/O:**
        - READ: `project_prd.md`, `automation_entities.md`, `definition_of_done_checklist.md`, `state_manager_instructions.md`, `project_ontology.md`.
        - CREATE/WRITE: `sprints.json` (initial list), `Sprint_1/sprint_description.md`. (If multiple sprints planned, create placeholders or initial descriptions: `Sprint_2/sprint_description.md`, etc.)
        - UPDATE: `activeContext.md` (reflecting completion of planning, next step is Task Generation for Sprint 1).
4. **NEXT Sprint Tasks Generation (Detailed by Entity Type)**
    
    This phase occurs after sprint planning (`sprint_description.md` is created) and before execution begins. The AI Agent reads the sprint goals and entity definitions to create specific, actionable tasks.
    
    **Common Inputs for all types:**
    
    - `Sprint_N/sprint_description.md`
    - `Project_Name/automation_entities.md` (for specs of entities in this sprint)
    - `Project_Name/project_ontology.md`
    - Relevant files from `System_Memory_Bank/` (e.g., `testing_definition.md`)
    
    **Common Outputs for all types:**
    
    - Entries added to `Sprint_N/tasks.json`
    - Entries added to `Sprint_N/tests.json`
    - Detailed `Sprint_N/Tasks/Task_*.md` files created
    - Detailed `Sprint_N/Tests/Task_*_Test_*.md` files created
    
    ---
    
    **1. Task Generation for Teams**
    
    - **Specific Inputs:** `System_Memory_Bank/Teams.md`, `System_Memory_Bank/deployment_pattern.md`
    - **Process:**
        1. **Identify Team(s):** Determine which Teams are scheduled for development in this sprint based on `sprint_description.md` and `automation_entities.md`.
        2. **Consult Guidelines:** Read `Teams.md` for structure, patterns, documenting and testing requirements.
        3. **Generate Test Tasks:**
            - Create tasks (`task_type: Testing`) to *write* the test code first (unit, integration). Often one task per major function or use case defined in `automation_entities.md` or `Teams.md` guidelines. Tag tests with project/sprint names within the task description (`Task_*.md`).
            - Create corresponding test definition files (`Tests/Task_*_Test_*.md`) detailing use cases.
            - Create entries in `tests.json` (status: Pending).
        4. **Generate Coding Tasks:**
            - Create task(s) (`task_type: Coding`) to *implement* the Team logic. Specify coding the Execution Team first, then the Evaluation Team (if applicable). Task description should reference relevant tests.
            - Query host assistant for relevant code samples or API usage examples based on team description and add to `Task_*.md`.
        5. **Generate Documentation Task:** Create a task (`task_type: Documentation`) to write/update docstrings and potentially a README section for the Team.
        6. **Generate Data Generation Task:** Create a task (`task_type: Data Generation`) to create sample input/output datasets for testing and fulfilling Definition of Done (DoD) criteria. Specify storage location (e.g., `auxiliary/generated_data/`).
        7. **Generate Project Test Execution Task:** *Conditional*: If the Team is considered "complete" within the sprint context (or at sprint end), create a task (`task_type: Testing`) to run *all relevant project tests* (not just sprint tests) against this team.
        8. **Generate Deployment Task:** Create a task (`task_type: Deployment`) to upload/register the completed Team to the central repository (e.g., MongoDB), referencing `deployment_pattern.md`.
        9. **Generate Update & Git Tasks:** Create standard tasks (`task_type: Update Context`, `task_type: Git`) for updating `activeContext.md`, relevant `.json` files (status updates), and performing Git operations (commit, push, PR).
        10. **Generate Definition Update Tasks:** *Conditional*: If development implies changes to I/O/D, create tasks to update `automation_entities_summary.md`, `automation_entities.md`, `project_ontology.md`, `state_manager_instructions.md`.
        11. **Generate Replanning Task:** *Conditional*: If the Team's Input, Output, or core Description changes significantly during development compared to the plan in `automation_entities.md`, create a task (`task_type: Workflow`, sub_type: Replanning) to trigger the replanning process.
    
    ---
    
    **2. Task Generation for Tools (Container & Internal)**
    
    - **Specific Inputs:** `System_Memory_Bank/Tools.md`
    - **Process:**
        1. **Identify Tool(s):** Determine which Tools are scheduled.
        2. **Consult Guidelines:** Read `Tools.md`.
        3. **Generate Test Tasks:** Create tasks (`task_type: Testing`) to write test code. Create `Tests/Task_*_Test_*.md` and entries in `tests.json`.
        4. **Generate Coding Tasks:** Create task(s) (`task_type: Coding`) to implement the Tool logic. Query host assistant if needed.
        5. **Generate Data Generation Task:** Create a task (`task_type: Data Generation`) for test datasets (inputs, expected outputs).
        6. **Generate Local Test Execution Task:** Create a task (`task_type: Testing`) to run the created tests using the generated data.
        7. **Generate Deployment/Update Task:** *Conditional*: For shared/online Tools, create a task (`task_type: Deployment`) to update the central repository (e.g., MongoDB tool DB) or deploy it.
        8. **Generate Online Test Execution Task:** *Conditional*: If deployed, create a task (`task_type: Testing`) to test the live/online tool.
        9. **Generate Documentation Task:** Create a task (`task_type: Documentation`).
        10. **Generate Update & Git Tasks:** Create standard update and Git tasks.
        11. **Generate Definition Update Tasks:** *Conditional*: If I/O/D changes, create tasks to update definition files.
        12. **Generate Replanning Task:** *Conditional*: If I/O/D changes significantly, create a replanning task.
    
    ---
    
    **3. Task Generation for Containers**
    
    - **Specific Inputs:** `System_Memory_Bank/Containers.md`
    - **Process:**
        1. **Identify Container(s):** Determine which Containers are scheduled.
        2. **Consult Guidelines:** Read `Containers.md` for structure (stages, variables) and logic patterns.
        3. **Generate Test Tasks:** Create tasks (`task_type: Testing`) to write integration tests for the Container's flow (testing interactions between stages, variable passing, conditional logic). Create `Tests/Task_*_Test_*.md` and entries in `tests.json`.
        4. **Generate Coding/Configuration Tasks:** Create task(s) (`task_type: Coding`) to define the Container (e.g., writing the YAML/JSON config or Python script defining stages, context variables, flow logic).
        5. **Generate Documentation Task:** Create a task (`task_type: Documentation`) explaining the container's purpose, flow, context variables, and configuration.
        6. **Generate Integration Test Execution Task:** Create a task (`task_type: Testing`) to run the integration tests defined earlier.
        7. **Generate Deployment Task:** *Conditional*: If containers need registration/deployment, create a task (`task_type: Deployment`).
        8. **Generate Update & Git Tasks:** Create standard update and Git tasks.
        9. **Generate Definition Update Tasks:** *Conditional*: If the container structure (stages, core logic) changes significantly, create tasks to update definition files.
        10. **Generate Replanning Task:** *Conditional*: If structure/logic deviates significantly from plan, create a replanning task.
    
    **4. Task Generation for Events**
    
    - **Specific Inputs:** `System_Memory_Bank/Events.md`
    - **Process:**
        1. **Identify Event Handler(s):** Determine which Event handlers are scheduled.
        2. **Consult Guidelines:** Read `Events.md` for schema definition, parsing, and integration patterns (e.g., Hookdeck).
        3. **Generate Data Generation Task:** Create a task (`task_type: Data Generation`) to generate sample event payloads (valid, invalid, edge cases) for testing/DoD. It can be triggering external events and logging them in the platform (not managed events).
        4. **Generate Test Tasks:** Create tasks (`task_type: Testing`) to write tests for the parsing logic and trigger validation. May include defining steps for *manual testing* if external interfaces are involved. Create `Tests/Task_*_Test_*.md` and entries in `tests.json`.
        5. **Generate Coding Tasks:** Create task(s) (`task_type: Coding`) to implement the event handler logic (parsing input, calling downstream components, interacting with event infrastructure).
        6. **Generate Documentation Task:** Create a task (`task_type: Documentation`) detailing the expected event schema, parsing rules, and triggered actions.
        7. **Generate Test Execution Task:** Create a task (`task_type: Testing`) to run the automated tests and log the steps/results of any manual tests.
        8. **Generate Update & Git Tasks:** Create standard update and Git tasks.
        9. **Generate Definition Update Tasks:** *Conditional*: If event schema or handling logic changes, create tasks to update definition files.
        10. **Generate Replanning Task:** *Conditional*: If schema/logic changes significantly, create a replanning task.
5. **NEXT Sprint Tasks Execution (Detailed by Entity Type)**
    
    This phase involves the AI Agent picking up a task from `tasks.json` (status 'Todo', dependencies met) and executing it based on its `Task_*.md` description.
    
    **Common Inputs for task execution:**
    
    - `Sprint_N/Tasks/Task_X.md` (Primary instructions)
    - Relevant `Sprint_N/Tests/Task_*_Test_*.md` files
    - Existing code in `Project_Name/src/`
    - `System_Memory_Bank/Debugging.md` (if errors occur)
    - `activeContext.md` (for recent context)
    
    **Common Outputs for task execution:**
    
    - Modified code in `Project_Name/src/`
    - Updated status in `Sprint_N/tasks.json` and `Sprint_N/tests.json`
    - Updated `Project_Name/activeContext.md`
    - Files created in `Project_Name/auxiliary/` (e.g., data, logs)
    - External interactions (Git push, DB updates, API calls)
    
    **1. Task Execution for Teams**
    
    - **Process based on `task_type`:**
        - **Testing (Write Test):** Read `Tests/Task_*_Test_*.md`, write test code in `src/tests/`, run test (expect fail), update `tasks.json` (task done), `tests.json` (test pending).
        - **Coding:** Read `Task_X.md`, write/modify Team code in `src/teams/`. Run associated sprint tests (from `tests.json`). If tests fail: consult `Debugging.md`, analyze logs, query host assistant, attempt fix, re-run tests. Once tests pass, update `tasks.json` (task done), update related entries in `tests.json` (test passed).
        - **Documentation:** Update docstrings in `src/teams/` or relevant markdown files as per `Task_X.md` with . Update `tasks.json`.
        - **Data Generation:** Create specified data files in `auxiliary/generated_data/` upload those to MongoDB datasets. Update `tasks.json`.
        - **Testing (Run Project Tests):** Execute the broader project test suite targeting the completed team. Update `tasks.json`, `tests.json` based on results.
        - **Deployment:** Read `deployment_pattern.md`, execute steps (e.g., script calls to update MongoDB). Update `tasks.json`.
        - **Update Context / Git / Update Definitions / Replanning:** Perform the specific actions described in `Task_X.md` (modify files, run git commands, trigger replanning workflow). Update `tasks.json`.
    - **End of Sprint:** AI Agent may be instructed (or automatically detect based on sprint completion) to start a new, clean dialogue context.
    
    ---
    
    **2. Task Execution for Tools (Container & Internal)**
    
    - **Process based on `task_type`:**
        - **Testing (Write Test):** Similar to Teams, write code in `src/tests/`.
        - **Coding:** Write/modify Tool code in `src/tools/container_tools/` or `src/tools/internal_tools/`. Run tests. Debug if needed. Update status files.
        - **Data Generation:** Create data in `auxiliary/generated_data/`.
        - **Testing (Run Local Test):** Execute tests using generated data. Update status files.
        - **Deployment:** Update tool registry (e.g., MongoDB) or deploy service as per `Task_X.md`.
        - **Testing (Run Online Test):** Interact with the deployed tool's API/endpoint. Update status files.
        - **Documentation / Update Context / Git / Update Definitions / Replanning:** Execute as per `Task_X.md`.
    
    ---
    
    **3. Task Execution for Containers**
    
    - **Process based on `task_type`:**
        - **Testing (Write Test):** Write integration test code in `src/tests/` focusing on container flow.
        - **Coding:** Write/modify Container definition files (e.g., YAML, Python script) in `src/containers/`.
        - **Testing (Run Integration Test):** Execute the integration tests against the container definition. Debug flow/logic errors. Update status files.
        - **Documentation / Deployment / Update Context / Git / Update Definitions / Replanning:** Execute as per `Task_X.md`.
    
    ---
    
    **4. Task Execution for Events**
    
    - **Process based on `task_type`:**
        - **Data Generation:** Create sample event payloads in `auxiliary/generated_data/`.
        - **Testing (Write Test):** Write test code for parsing/handling in `src/tests/`. If manual steps are needed, log them clearly in the test execution task description.
        - **Coding:** Write/modify event handling code in `src/events/`.
        - **Testing (Run Test):** Execute automated tests using sample data. If manual steps exist: Log instructions for the human, await confirmation/input, log result. Update status files.
        - **Documentation / Update Context / Git / Update Definitions / Replanning:** Execute as per `Task_X.md`.
6. **Project Re-planning:**
    - **Trigger:** Significant change detected or requested (e.g., PRD update, change in core entity I/O/D during development, explicit developer request). Task execution might generate a specific "replanning task".
    - **Action (AI Agent):**
        - Reads updated source files (`project_prd.md`, `automation_entities.md`, etc.).
        - Reads `activeContext.md`, `sprints.json`.
        - Consults `System_Memory_Bank/replanning.md`.
        - Analyzes the impact of the changes on the existing plan (sprints, tasks).
        - Regenerates affected sprint descriptions and task lists. Updates dependencies. May involve adding, removing, or modifying sprints/tasks.
        - Optionally queries "host assistant" again if new components are needed or existing ones change significantly.
    - **File I/O:**
        - READ: Updated definition files, `activeContext.md`, `sprints.json`, `System_Memory_Bank/replanning.md`.
        - WRITE/MODIFY: `sprints.json`, affected `Sprint_N/sprint_description.md`, `Sprint_N/tasks.json`, `Sprint_N/tests.json`, potentially `Sprint_N/Tasks/Task_*.md`.
        - UPDATE: `activeContext.md` (reflecting re-planning activity and new next steps).
7. **Sprint/Project Completion:**
    - **Trigger:** All tasks in the final sprint are 'done', or project goals met.
    - **Action (AI Agent):**
        - Verifies all tasks and tests in relevant `.json` files are complete.
        - Performs final deployment/handover tasks.
        - Updates `sprints.json` to mark the final sprint/project as 'completed'.
        - Updates `activeContext.md` to reflect project completion.
    - **File I/O:**
        - READ: `sprints.json`, `Sprint_N/tasks.json`, `Sprint_N/tests.json`, `definition_of_done_checklist.md`.
        - WRITE/MODIFY: `sprints.json`, `activeContext.md`.

## **3. JSON File Samples**

**`Project_Name/sprints.json`**

**JSON**

`[
  {
    "sprint_id": "Sprint_1",
    "summary": "Initial setup, Core Transcription Team, Basic Notion Output Tool",
    "status": "In Progress", // Options: 'Planned', 'Tasks Generated', 'In Progress', 'Completed', 'Blocked'
    "start_date": "2025-04-28",
    "end_date": "2025-05-09",
    "description_file": "Sprint_1/sprint_description.md",
    "task_file": "Sprint_1/tasks.json",
    "test_file": "Sprint_1/tests.json"
  },
  {
    "sprint_id": "Sprint_2",
    "summary": "Action Item Extraction Team, Human-Proxy Notification Team, Retool Frontend Integration",
    "status": "Planned",
    "start_date": "2025-05-12",
    "end_date": "2025-05-23",
    "description_file": "Sprint_2/sprint_description.md",
    "task_file": "Sprint_2/tasks.json",
    "test_file": "Sprint_2/tests.json"
  }
]`

**`Project_Name/Sprint_1/tasks.json`**

**JSON**

`[
  {
    "task_id": "S1_T1",
    "summary": "Code Test for Transcription Team (Basic Case)",
    "status": "Done", // Options: 'Todo', 'In Progress', 'Done', 'Blocked'
    "dependencies": [],
    "component_type": "Team",
    "component_name": "TranscriptionTeam",
    "task_type": "Testing", // Options: 'Testing', 'Coding', 'Documentation', 'Data Generation', 'Deployment', 'Infra', 'Update Context', 'Git'
    "detail_file": "Tasks/Task_1.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 1
  },
  {
    "task_id": "S1_T2",
    "summary": "Code Transcription Team (Initial Version)",
    "status": "In Progress",
    "dependencies": ["S1_T1"],
    "component_type": "Team",
    "component_name": "TranscriptionTeam",
    "task_type": "Coding",
    "detail_file": "Tasks/Task_2.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 3
  },
  {
    "task_id": "S1_T3",
    "summary": "Code Test for Notion Output Tool (Basic Case)",
    "status": "Todo",
    "dependencies": [],
    "component_type": "Container Tool",
    "component_name": "NotionOutputTool",
    "task_type": "Testing",
    "detail_file": "Tasks/Task_3.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 1
  },
  {
    "task_id": "S1_T4",
    "summary": "Code Notion Output Container Tool",
    "status": "Todo",
    "dependencies": ["S1_T3"],
    "component_type": "Container Tool",
    "component_name": "NotionOutputTool",
    "task_type": "Coding",
    "detail_file": "Tasks/Task_4.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 2
  },
   {
    "task_id": "S1_T5",
    "summary": "Update activeContext.md after completing TranscriptionTeam",
    "status": "Todo",
    "dependencies": ["S1_T2"], // Depends on coding being done
    "component_type": "Workflow",
    "component_name": "ContextManagement",
    "task_type": "Update Context",
    "detail_file": "Tasks/Task_5.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 0.5
  },
  {
    "task_id": "S1_T6",
    "summary": "Commit and Push Sprint 1 Initial Code",
    "status": "Todo",
    "dependencies": ["S1_T2", "S1_T4"], // Depends on initial coding tasks
    "component_type": "Workflow",
    "component_name": "VersionControl",
    "task_type": "Git",
    "detail_file": "Tasks/Task_6.md",
    "assigned_to": "AI Agent",
    "estimated_effort_pts": 0.5
  }
]`

**`Project_Name/Sprint_1/tests.json`**

**JSON**

`[
  {
    "test_id": "S1_Test_T1_1",
    "task_id": "S1_T1", // Links to the task that creates this test code
    "summary": "Verify TranscriptionTeam handles basic audio input correctly",
    "status": "Active", // Options: 'ON HOLD' //if is is not relevant anymore
    "dependencies": [], // Test dependencies (e.g., Test B needs Test A setup)
    "detail_file": "Tests/Task_1_Test_1.md",
    "execution_task_id": "S1_T2" // Links to the task whose successful execution should make this test pass
  },
  {
    "test_id": "S1_Test_T3_1",
    "task_id": "S1_T3",
    "summary": "Verify NotionOutputTool creates a page with correct title and basic content",
    "status": "Pending",
    "dependencies": [],
    "detail_file": "Tests/Task_3_Test_1.md",
    "execution_task_id": "S1_T4"
  }
]`

## **4. MD File Summaries**

- **`System_Memory_Bank/Teams.md`**: Provides templates, schema definitions (Input/Output/Descriptions), best practices, required documentation patterns, testing strategies (e.g., defining evaluation teams), and data generation instructions specifically for creating Radical100 **Teams**. Includes examples for different team types (LiteLLM, Autogen, etc.).
- **`System_Memory_Bank/Tools.md`**: Similar to `Teams.md`, but focused on Radical100 **Container Tools** and **Internal Tools**. Defines expected schemas, coding standards, testing approaches (including data generation for DoD), and documentation requirements for tools.
- **`System_Memory_Bank/Events.md`**: Guidelines for defining and handling **Events**. Covers schema definition, parsing logic, integration patterns (e.g., with Hookdeck), triggering mechanisms for Containers/Tasks, and testing strategies (including potential human steps for external events).
- **`System_Memory_Bank/Containers.md`**: Defines patterns and best practices for creating Radical100 **Containers**. Includes schemas for context variables, step definitions, guidance on choosing container types (FlowchartExecutor, MultiStageTeamV2), defining conditional logic, error handling, and documentation standards.
- **`System_Memory_Bank/deployment_pattern.md`**: Outlines standard procedures for deploying components (Teams, Tools). May include checklists, environment considerations, instructions for updating databases (e.g., MongoDB tool registry), and rollback procedures.
- **`System_Memory_Bank/testing_definition.md`**: Describes the overall testing philosophy and standards for the framework. Covers unit testing, integration testing, end-to-end testing, requirements for test data, evaluation metrics, and potentially links to specific testing libraries or frameworks.
- **`System_Memory_Bank/Debugging.md`**: Provides a structured approach to debugging common issues encountered during development. May include steps for analyzing logs, common error types, strategies for isolating problems, and instructions for using debugging tools or querying the host assistant effectively.
- **`System_Memory_Bank/replanning.md`**: Defines the triggers and process for initiating a replanning cycle. Outlines how to assess the impact of changes, which artifacts need updating, and the steps the AI agent should follow to revise the project plan (sprints, tasks).
- **`Project_Name/activeContext.md`**: A dynamic, frequently updated file acting as the AI agent's short-term memory for the project. Contains the current work focus, recent changes made, identified next steps, active decisions/considerations, important patterns specific to the project, and key learnings or insights gathered during development.
- **`Project_Name/project_prd.md`**: The formal Product Requirements Document detailing the goals, features, user stories, constraints, and overall scope of the project. Serves as the primary input for planning and definition.
- **`Project_Name/project_ontology.md`**: Defines the key terms, concepts, entities, and their relationships within the project's domain. Provides a shared vocabulary for the AI agent and human developers, ensuring consistency.
- **`Project_Name/automation_entities_summary.md`**: A high-level summary table or list of all the planned Radical100 components (Teams, Tools, Containers, Events) for the project. Includes name, brief description, and high-level Input/Output/Description (I/O/D).
- **`Project_Name/automation_entities.md`**: Provides the full, detailed specification for each planned Radical100 component, following the structure requested in the "Radical100 framework development definition" (Detailed Description, Input Schema, Output Schema, Internal Tools Used, Execution Flow/Steps).
- **`Project_Name/state_manager_instructions.md`**: Defines project-specific rules and conventions for managing state via Container Context Variables. Specifies naming conventions, data types, initialization rules, and how variables should be updated by different components.
- **`Project_Name/definition_of_done_checklist.md`**: A checklist outlining the criteria that must be met for the project (or potentially a major feature/sprint) to be considered complete. Includes aspects like code completion, testing coverage, documentation, deployment, and user acceptance.
- **`Project_Name/Sprint_N/sprint_description.md`**: Details the specific goals, requirements, scope, deliverables, and Definition of Done (DoD) for a particular sprint (Sprint N). Lists the main components to be developed or integrated during the sprint.
- **`Project_Name/Sprint_N/Tasks/Task_X.md`**: A detailed description of a single development task (Task X) within Sprint N. Includes a clear description, acceptance criteria, specific requirements, expected Input/Output/Data (I/O/D) if applicable, and step-by-step instructions for the AI agent to execute the task.
- **`Project_Name/Sprint_N/Tests/Task_X_Test_Y.md`**: Describes a specific test case (Test Y) related to a task (Task X). Includes a description of the test's purpose and detailed use cases or scenarios to be verified. This guides the creation of automated test code or manual test procedures.

**System Memory Bank Files**
These files contain reusable knowledge, patterns, and guidelines for the Radical100 framework and the development process.
**`System_Memory_Bank/Teams.md`**
*Purpose: Defines standards, patterns, and guidelines for developing Radical100 Teams.*
1. **Introduction**
    ◦ Purpose of Teams in Radical100
    ◦ Overview of different Team types
    ◦ How this document guides Team development
2. **General Team Principles**
    ◦ Core responsibilities (execution logic, tool usage)
    ◦ Interaction with Containers (Input/Output via Context Variables)
    ◦ State management within Teams (if applicable)
    ◦ Idempotency considerations
3. **Standard Team Schema Definition**
    ◦ Required metadata (Name, Description, Version)
    ◦ Input Schema Definition (Structure, Data Types, Sources - typically Container Variables)
    ◦ Output Schema Definition (Structure, Data Types, Destinations - typically Container Variables)
    ◦ Internal Tools Usage Declaration
4. **Team Type Specific Guidelines**
    ◦ **LiteLLMTeamV2**
        ▪ Configuration (Model selection, parameters)
        ▪ Prompting strategies and templates
        ▪ Input/Output mapping examples
        ▪ Use cases (Summarization, Extraction, Classification)
    ◦ **AutogenAssistantTeam**
        ▪ Agent configuration (LLM config, system message)
        ▪ Internal Tool definition and integration
        ▪ Function calling schema
        ▪ Use cases (API interaction, complex calculations)
    ◦ **AutogenGroupchatTeam**
        ▪ Defining agent roles and system messages
        ▪ Managing conversation flow and termination
        ▪ Tool usage across multiple agents
        ▪ Use cases (Collaborative problem solving, multi-perspective analysis)
    ◦ **OpenAIAssistant**
        ▪ Configuration and setup
        ▪ Tool integration specifics
        ▪ Use cases
    ◦ **LlamaIndexWorkflow**
        ▪ Workflow definition
        ▪ Task management patterns
        ▪ Use cases
    ◦ **Human-Proxy Team**
        ▪ Capabilities (Messaging channels: Slack, Email, Teams)
        ▪ Input schema for sending messages (User ID, Channel, Content)
        ▪ Output schema for received messages/confirmations
        ▪ Context management for conversations
        ▪ Use cases (Notifications, approvals, data gathering)
    ◦ **Special Task Management Teams (MapReduce, BatchExecutor)**
        ▪ Configuration and use cases
5. **Development Workflow & Best Practices**
    ◦ Naming conventions
    ◦ Code structure recommendations
    ◦ Error handling patterns
    ◦ Logging standards
6. **Testing Teams**
    ◦ Unit testing strategies (mocking dependencies, Internal Tools)
    ◦ Integration testing within Containers
    ◦ Defining Evaluation Teams (Purpose, Input/Output, Metrics)
    ◦ Test data generation requirements and examples
    ◦ Test tagging conventions (Project, Sprint)
7. **Documentation Standards**
    ◦ Docstring requirements (Input, Output, Purpose, Tools used)
    ◦ README generation guidelines
8. **Sample Team Definitions**
    ◦ Example snippets for different team types
9. **Deployment Checklist (Team Specific)**
    ◦ Steps for registering/updating Teams in a central repository (if applicable)
**`System_Memory_Bank/Tools.md`**
*Purpose: Defines standards, patterns, and guidelines for developing Radical100 Container Tools and Internal Tools.*
1. **Introduction**
    ◦ Distinction between Container Tools and Internal Tools
    ◦ Role of Tools in the framework (interacting with external systems, complex logic)
2. **Container Tools**
    ◦ **Purpose:** Executed as stages within Containers, interact via Context Variables.
    ◦ **Schema Definition:**
        ▪ Required metadata (Name, Description, Version)
        ▪ Input Schema (from Container Context Variables)
        ▪ Output Schema (updating Container Context Variables)
    ◦ **Development Guidelines:**
        ▪ Code structure (Python scripts/functions)
        ▪ Dependency management
        ▪ Error handling (reporting back to Container)
        ▪ Logging standards
    ◦ **Testing:**
        ▪ Unit testing individual functions
        ▪ Integration testing within a sample Container
        ▪ Test data requirements
    ◦ **Use Cases:** API calls, database interactions, complex data transformations, interacting with frontends.
    ◦ **Sample Container Tool Definitions**
3. **Internal Tools**
    ◦ **Purpose:** Used *by* Agents *within* Teams (primarily Autogen/OpenAI Assistants).
    ◦ **Schema Definition:**
        ▪ Function signature definition (for LLM function calling)
        ▪ Input parameters (passed by the Agent)
        ▪ Output/Return value (returned to the Agent)
    ◦ **Development Guidelines:**
        ▪ Code structure
        ▪ Error handling (returning informative errors to the Agent)
        ▪ Security considerations (API keys, permissions)
    ◦ **Testing:**
        ▪ Unit testing the tool's function directly
    ◦ **Use Cases:** Specific API wrappers, complex calculations needed by an Agent, file system access.
    ◦ **Sample Internal Tool Definitions**
4. **General Best Practices (Both Tool Types)**
    ◦ Naming conventions
    ◦ Idempotency considerations
    ◦ Configuration management (API keys, endpoints)
5. **Documentation Standards**
    ◦ Docstring requirements (Input, Output, Purpose, Side Effects)
6. **Deployment Checklist (Tool Specific)**
    ◦ Steps for registering/updating Tools in a central repository (if applicable)
**`System_Memory_Bank/Events.md`**
*Purpose: Defines standards for handling external events within the Radical100 framework.*
1. **Introduction**
    ◦ Purpose of Event handling (triggering workflows from external sources)
    ◦ Integration with external systems (Webhooks, Message Queues)
    ◦ Role of services like Hookdeck (optional)
2. **Event Handling Workflow**
    ◦ Receiving Events (Webhook endpoint definition)
    ◦ Initial Parsing & Validation (Extracting key information, schema validation)
    ◦ Routing Events (Determining which Container/Task to trigger)
    ◦ Acknowledging Events
3. **Event Schema Definition**
    ◦ Standard header requirements (Source, Event Type, Timestamp, Event ID)
    ◦ Payload structure recommendations (JSON)
    ◦ Versioning strategies
4. **Developing Event Handlers**
    ◦ Code structure (e.g., specific functions/modules for different event types)
    ◦ Parsing logic implementation
    ◦ Triggering downstream processes (e.g., initiating a Container)
    ◦ Error handling (failed parsing, downstream errors)
    ◦ Logging standards
5. **Testing Event Handlers**
    ◦ Generating sample event payloads (valid, invalid, edge cases)
    ◦ Unit testing parsing logic
    ◦ Integration testing the trigger mechanism
    ◦ Manual testing procedures for external interface triggers (logging requirements)
6. **Documentation Standards**
    ◦ Documenting expected event schemas
    ◦ Explaining parsing rules and triggered actions
7. **Sample Event Definitions & Handler Snippets
`System_Memory_Bank/Containers.md`**
*Purpose: Defines standards and patterns for developing Radical100 Containers.*
1. **Introduction**
    ◦ Purpose of Containers (Orchestrating multi-stage workflows)
    ◦ Managing state and context via Context Variables
    ◦ Overview of Container Types
2. **General Container Principles**
    ◦ Defining clear boundaries and responsibilities
    ◦ Modularity and reusability
3. **Container Schema Definition**
    ◦ Required metadata (Name, Description, Version, Container Type)
    ◦ Context Variable Definition:
        ▪ Naming conventions
        ▪ Data types
        ▪ Initial values / Origin (Webhook Input, Default, etc.)
        ▪ Purpose/Usage notes
    ◦ Stage/Step Definition:
        ▪ Stage ID/Name
        ▪ Component to execute (Team Name or Container Tool Name)
        ▪ Input mapping (Context Variables -> Component Input)
        ▪ Output mapping (Component Output -> Context Variables)
        ▪ Conditional execution logic (based on Context Variables)
        ▪ Error handling configuration for the stage
4. **Container Type Specific Guidelines**
    ◦ **MultiStageTeamV2:**
        ▪ Defining stage dependencies
        ▪ Linear vs. parallel execution patterns
        ▪ Use cases (Sequential processing pipelines)
    ◦ **FlowchartExecutor:**
        ▪ Defining flowchart logic (nodes, edges, conditions)
        ▪ Implementing loops and branching
        ▪ Use cases (Complex conditional workflows, state machines)
5. **Development Workflow & Best Practices**
    ◦ Designing container flows
    ◦ Managing complex state
    ◦ Error handling strategies (retries, fallback paths)
    ◦ Logging within containers (tracking stage execution and variable changes)
6. **Testing Containers**
    ◦ Defining integration test scenarios
    ◦ Mocking Team/Tool dependencies
    ◦ Asserting Context Variable changes and final state
    ◦ Testing conditional logic and error paths
    ◦ Test data requirements
7. **Documentation Standards**
    ◦ Visualizing the flow (e.g., Mermaid diagrams)
    ◦ Documenting Context Variables (purpose, origin, usage)
    ◦ Explaining stage logic and conditions
8. **Sample Container Definitions**
    ◦ Example snippets for different container types and flows
9. **Deployment Checklist (Container Specific)**
    ◦ Steps for registering/deploying Containers (if applicable)
**`System_Memory_Bank/deployment_pattern.md`**
*Purpose: Outlines standard procedures and checklists for deploying Radical100 components.*
1. **Introduction**
    ◦ Deployment goals (Consistency, Reliability, Traceability)
    ◦ Overview of deployment targets (e.g., Central Registry, Serverless Functions, Container Orchestrator)
2. **Pre-Deployment Checklist**
    ◦ Code review completion
    ◦ All tests passing (Unit, Integration)
    ◦ Documentation updated
    ◦ Dependencies verified
    ◦ Configuration finalized (Environment variables, secrets)
    ◦ Version updated
3. **Deployment Procedures (by Component Type)**
    ◦ Deploying Teams (e.g., updating registry, deploying evaluation logic)
    ◦ Deploying Container Tools (e.g., updating registry, deploying script/service)
    ◦ Deploying Internal Tools (often bundled with Teams)
    ◦ Deploying Containers (e.g., updating registry, deploying definition)
    ◦ Deploying Event Handlers (e.g., updating webhook endpoint, deploying handler code)
4. **Post-Deployment Checklist**

    ◦ Smoke tests / Basic functionality checks in target environment
    ◦ Monitoring setup verification
    ◦ Logging verification
    ◦ Announce deployment / Update status trackers
5. **Rollback Procedures**
    ◦ Steps to revert to a previous stable version
    ◦ Identifying rollback triggers
6. **Environment Specific Considerations**
    ◦ Development vs. Staging vs. Production environments
**`System_Memory_Bank/testing_definition.md`**
*Purpose: Defines the overall testing strategy, standards, and methodologies.*
1. **Introduction**
    ◦ Importance of testing in AI-driven development
    ◦ Testing philosophy (Test-Driven Development principles, levels of testing)
2. **Levels of Testing**
    ◦ **Unit Testing:**
        ▪ Scope (Individual functions, methods, tool logic)
        ▪ Mocking dependencies (Internal Tools, external APIs)
        ▪ Recommended frameworks/libraries
    ◦ **Integration Testing:**
        ▪ Scope (Interaction between components: Team-Tool, Container-Team, Container-Tool, Event-Container)
        ▪ Testing data flow and context variable manipulation
        ▪ Testing conditional logic in Containers
    ◦ **End-to-End (E2E) Testing:**
        ▪ Scope (Full workflow from trigger event to final output)
        ▪ Simulating real-world scenarios
        ▪ Handling external system interactions
    ◦ **Evaluation Testing (for LLM-based Teams):**
        ▪ Defining evaluation metrics (Accuracy, Relevance, Format adherence, etc.)
        ▪ Role of Evaluation Teams
        ▪ Golden datasets / Reference outputs
3. **Test Data Management**
    ◦ Requirements for test data (realistic, diverse, edge cases)
    ◦ Strategies for generating test data (manual, synthetic)
    ◦ Storing and managing test datasets (`auxiliary/generated_data/`)
4. **Testing Standards & Conventions**
    ◦ Test code structure and organization (`src/tests/`)
    ◦ Naming conventions for tests
    ◦ Test tagging (`Project`, `Sprint`, `ComponentType`)
    ◦ Code coverage targets (optional)
5. **Test Execution & Reporting**
    ◦ Running tests (manual triggers, CI/CD integration)
    ◦ Interpreting test results
    ◦ Reporting failures
6. **Testing Specific Component Types**
    ◦ Specific considerations for testing Teams, Tools, Containers, Events
**`System_Memory_Bank/Debugging.md`**
*Purpose: Provides guidance on diagnosing and resolving issues during development.*
1. **Introduction**
    ◦ Common challenges in debugging AI agent workflows
    ◦ General debugging principles (Isolate, Reproduce, Analyze)
2. **Debugging Workflow**
    ◦ Step 1: Identify the Failing Component/Task
    ◦ Step 2: Gather Information (Logs, Error Messages, `activeContext.md`)
    ◦ Step 3: Reproduce the Issue (Using specific inputs/test cases)
    ◦ Step 4: Analyze the Problem (Code logic, data issues, configuration errors, prompt issues)
    ◦ Step 5: Formulate & Test Hypothesis/Fix
    ◦ Step 6: Verify the Fix (Re-run tests)
    ◦ Step 7: Document Learnings (`activeContext.md`)
3. **Common Issues & Solutions (by Component Type)**
    ◦ **Teams:** Prompt failures, unexpected LLM output, tool execution errors, incorrect I/O mapping.
    ◦ **Tools:** API errors, incorrect data transformation, permission issues, dependency conflicts.
    ◦ **Containers:** Incorrect state propagation (Context Variables), faulty conditional logic, stage execution failures, infinite loops.
    ◦ **Events:** Parsing errors, incorrect routing, trigger failures.
4. **Using Logging Effectively**
    ◦ Standard logging levels and formats
    ◦ Tracking key variables and decisions
    ◦ Correlating logs across components
5. **Debugging Techniques**
    ◦ Step-through debugging (if IDE supports)
    ◦ Analyzing LLM inputs/outputs directly
    ◦ Simplifying the test case
    ◦ Consulting `System_Memory_Bank` documentation
    ◦ Querying the host assistant for suggestions
6. **Escalation Path** (When to involve human developer)
**`System_Memory_Bank/replanning.md`**
*Purpose: Defines the process for revising the project plan when significant changes occur.*
1. **Introduction**
    ◦ Why replanning is necessary
    ◦ Goal: Adapt to changes while maintaining project integrity
2. **Replanning Triggers**
    ◦ Significant changes in `project_prd.md`
    ◦ Changes to core I/O/D of planned `automation_entities.md` discovered during development
    ◦ Major dependency changes
    ◦ External factors (e.g., API deprecation)
    ◦ Explicit request from developer
    ◦ Completion of a "Replanning Task" generated during task execution
3. **Replanning Process**
    ◦ Step 1: Identify the Scope of Change (Read updated definitions, `activeContext.md`)
    ◦ Step 2: Assess Impact on Existing Plan (`sprints.json`, `Sprint_N/tasks.json`, dependencies)
    ◦ Step 3: Consult Original Requirements & Definitions (`project_prd.md`, `automation_entities.md`)
    ◦ Step 4: Determine Necessary Actions (Modify/Add/Remove Sprints, Tasks, Tests)
    ◦ Step 5: Query Host Assistant (Optional - identify reusable components for new requirements)
    ◦ Step 6: Update Planning Artifacts (`sprints.json`, `Sprint_N/sprint_description.md`, `Sprint_N/tasks.json`, `Sprint_N/tests.json`)
    ◦ Step 7: Update Definition Artifacts (If source definitions changed: `automation_entities.md`, etc.)
    ◦ Step 8: Update `activeContext.md` (Summarize replanning, state new focus)
4. **Considerations During Replanning**
    ◦ Minimizing disruption to ongoing work
    ◦ Maintaining traceability of changes
    ◦ Communicating changes (via `activeContext.md`)
**Project Specific Files (`Project_Name/`)**
These files contain information tailored to a single development project.
**`Project_Name/activeContext.md`**
Purpose: Dynamic short-term memory for the AI agent, tracking the immediate state of the project development.
(Note: This file's content changes constantly. The index represents the types of information typically present.)
1. **Current Work Focus**
    ◦ Active Sprint ID (e.g., `Sprint_1`)
    ◦ Current Task ID being worked on (e.g., `S1_T2`)
    ◦ Specific goal of the current session/interaction
2. **Recent Changes & Actions**
    ◦ Summary of the last few tasks completed
    ◦ Files modified/created recently
    ◦ Key outputs generated (e.g., "TranscriptionTeam initial coding complete, basic test passing")
    ◦ Decisions made (e.g., "Chose LiteLLMTeamV2 for summarization")
3. **Next Steps & Pending Actions**
    ◦ Identified next task ID(s) based on `tasks.json` and dependencies
    ◦ Questions for the developer (if any)
    ◦ Reminders (e.g., "Need to run full integration tests after Tool deployment")
4. **Active Decisions & Considerations**
    ◦ Open questions being evaluated
    ◦ Alternative approaches being considered
    ◦ Potential risks or blockers identified
5. **Important Patterns & Preferences (Project Specific)**
    ◦ Specific coding styles or libraries preferred for this project
    ◦ Key architectural decisions relevant to current work
6. **Learnings & Project Insights**
    ◦ Observations made during development (e.g., "API X has strict rate limits")
    ◦ Unexpected challenges encountered
    ◦ Successful patterns identified within the project
**`Project_Name/project_prd.md`**
*Purpose: Formal requirements document for the project.*
1. **Introduction & Goals**
    ◦ Project vision and objectives
    ◦ High-level summary of the desired outcome
2. **Scope**
    ◦ In-scope features and functionality
    ◦ Out-of-scope items
3. **User Stories / Use Cases**
    ◦ Description of user interactions and desired system behaviors
4. **Functional Requirements**
    ◦ Detailed breakdown of what the system must do
    ◦ Data inputs and outputs
    ◦ Processing logic
5. **Non-Functional Requirements**
    ◦ Performance targets (e.g., latency, throughput)
    ◦ Scalability needs
    ◦ Security requirements
    ◦ Reliability / Availability targets
    ◦ Usability considerations
6. **External Interfaces / Dependencies**
    ◦ Required interactions with other systems, APIs, or data sources
7. **Assumptions & Constraints**
    ◦ Technical or business limitations
    ◦ Assumptions made during requirement definition
**`Project_Name/project_ontology.md`**
*Purpose: Defines the key concepts, entities, and relationships specific to this project's domain.*
1. **Introduction**
    ◦ Purpose of the ontology for this project
2. **Core Entities**
    ◦ Definition of key nouns/objects in the domain (e.g., "Meeting", "Transcript", "Action Item", "User")
    ◦ Attributes of each entity
3. **Relationships**
    ◦ How entities relate to each other (e.g., "Meeting HAS Transcript", "Transcript CONTAINS Action Items", "Action Item ASSIGNED_TO User")
4. **Key Processes / Verbs**
    ◦ Definitions of important actions (e.g., "Summarize", "Transcribe", "Notify", "Extract")
5. **Controlled Vocabularies / Enums**
    ◦ Defined sets of values for specific attributes (e.g., Status: Pending, InProgress, Complete)
6. **Glossary of Terms
`Project_Name/automation_entities_summary.md`**
*Purpose: A high-level, quick-reference overview of the planned Radical100 components.*
1. **Project Name & Overview**
2. **Summary Table/List**
    ◦ **Component Name:** (e.g., `TranscriptionTeam`, `NotionOutputTool`, `MeetingProcessingContainer`)
    ◦ **Component Type:** (Team, Container Tool, Internal Tool, Container, Event)
    ◦ **Brief Description:** (Concise summary of purpose)
    ◦ **High-Level Input:** (Key data inputs)
    ◦ **High-Level Output:** (Key data outputs)
    ◦ **Dependencies:** (Other components it relies on)
    ◦ **Planned Sprint:** (Sprint ID where it's scheduled)
**`Project_Name/automation_entities.md`**
Purpose: Detailed specifications for each planned Radical100 component.
(Structure repeats for each component)
1. **Component: [Component Name]** (e.g., `TranscriptionTeam`)
    ◦ **Component Type:** (e.g., `Team`, `LiteLLMTeamV2`)
    ◦ **Description:** Detailed explanation of function and purpose.
    ◦ **Input Schema:**
        ▪ Variable Name | Data Type | Source (Context Variable) | Description
        ▪ `audio_data` | `bytes` | `Container.audio_blob` | Raw audio content
        ▪ `language_hint` | `str` | `Container.source_language` | Optional language hint
    ◦ **Output Schema:**
        ▪ Variable Name | Data Type | Destination (Context Variable) | Description
        ▪ `transcript_text` | `str` | `Container.raw_transcript` | Full transcribed text
        ▪ `transcription_status` | `str` | `Container.transcription_phase_status` | 'Success' or 'Error'
    ◦ **Internal Tools Used:** (List names, e.g., `transcription_api_tool`)
    ◦ **Execution Flow/Steps:**
        1. Receive `audio_data` and `language_hint` from input.
        2. Validate inputs.
        3. (If using Internal Tool) Prepare parameters for `transcription_api_tool`.
        4. (If using Internal Tool) Invoke `transcription_api_tool` with parameters.
        5. (If LiteLLMTeamV2) Construct prompt using input data.
        6. (If LiteLLMTeamV2) Call LLM via LiteLLM.
        7. Receive/Parse response (from Tool or LLM).
        8. Handle potential errors from Tool/LLM.
        9. Format output according to Output Schema (`transcript_text`, `transcription_status`).
        10. Return results.
    ◦ **Rationale/Design Notes:** (Optional: Why this approach was chosen)
    ◦ **Dependencies:** (Other components required before this one)
    ◦ **Planned Sprint:** (Sprint ID)
2. **Component: [Next Component Name]**
    ◦ ... (Repeat structure)
**`Project_Name/state_manager_instructions.md`**
*Purpose: Project-specific rules for defining and managing Container Context Variables.*
1. **Introduction**
    ◦ Importance of consistent state management
2. **Naming Conventions**
    ◦ Prefixes/Suffixes (e.g., `input_`, `status_`, `result_`)
    ◦ Case style (e.g., `snake_case`)
3. **Data Type Standards**
    ◦ Preferred types for common data (e.g., use ISO 8601 for timestamps)
4. **Variable Initialization**
    ◦ Rules for setting default values
    ◦ Identifying variables populated by initial triggers (e.g., Webhook)
5. **Variable Update Patterns**
    ◦ Who updates which variables (Teams vs. Tools)
    ◦ Handling status variables (e.g., standard values for 'Pending', 'Success', 'Error')
    ◦ Rules for overwriting vs. appending data (e.g., for lists)
6. **Scope and Lifetime**
    ◦ Defining variables specific to certain phases or loops within a Container
7. **Project-Specific Variable Glossary** (Optional: Central list of key variables and their purpose)
**`Project_Name/definition_of_done_checklist.md`**
*Purpose: Project-specific checklist defining criteria for completion.*
1. **Overall Project DoD**
    ◦ All planned features implemented as per `project_prd.md`.
    ◦ All E2E tests passing.
    ◦ Code coverage meets target (if applicable).
    ◦ All documentation complete (Code, Components, Project).
    ◦ Deployment to target environment successful.
    ◦ User Acceptance Testing (UAT) passed (if applicable).
    ◦ Performance targets met.
    ◦ Security review passed.
2. **Sprint DoD**
    ◦ All tasks in `tasks.json` for the sprint are 'Done'.
    ◦ All tests in `tests.json` for the sprint are 'Passed' or 'Skipped' (with reason).
    ◦ Sprint deliverables integrated into the main branch.
    ◦ Sprint review/demo completed (if applicable).
3. **Feature/Component DoD**
    ◦ Code implemented according to standards.
    ◦ Unit and Integration tests written and passing.
    ◦ Documentation (docstrings, README sections) complete.
    ◦ Relevant test data generated.
    ◦ Component successfully integrated within its Container(s).
    ◦ Meets relevant non-functional requirements.
**Sprint Specific Files (`Project_Name/Sprint_N/`)**
These files detail the plan and execution artifacts for a specific sprint.
**`Project_Name/Sprint_N/sprint_description.md`**
*Purpose: Outlines the goals, scope, and requirements for a specific sprint.*
1. **Sprint ID:** (e.g., `Sprint_1`)
2. **Sprint Goal:** (Concise statement of the main objective for this sprint)
3. **Dates:** (Start Date, End Date)
4. **Scope & Deliverables:**
    ◦ List of features/components to be developed/integrated in this sprint (referencing `automation_entities.md`)
    ◦ Specific user stories addressed
5. **Requirements:**
    ◦ Key functional/non-functional requirements relevant to this sprint's scope
6. **Working Directory:** (Primary source code paths relevant to this sprint)
7. **Definition of Done (Sprint Specific):**
    ◦ Reference to the general `definition_of_done_checklist.md`
    ◦ Any sprint-specific completion criteria
8. **Assumptions/Dependencies:**
    ◦ Assumptions made for this sprint's planning
    ◦ Dependencies on previous sprints or external factors
**`Project_Name/Sprint_N/Tasks/Task_X.md`**
*Purpose: Detailed instructions for the AI agent to execute a single task.*
1. **Task ID:** (e.g., `S1_T2`)
2. **Summary:** (Matches summary in `tasks.json`)
3. **Component Type:** (Team, Tool, Container, Event, Workflow)
4. **Component Name:** (Specific entity being worked on)
5. **Task Type:** (Testing, Coding, Documentation, Data Generation, Deployment, etc.)
6. **Description:** Detailed explanation of what needs to be done.
7. **Acceptance Criteria:** Measurable conditions that must be met for the task to be considered complete.
8. **Requirements:**
    ◦ Specific inputs needed (e.g., data files, configuration values)
    ◦ References to relevant documentation (`System_Memory_Bank/*`, `automation_entities.md`)
    ◦ Code samples or specific instructions from host assistant (if generated)
9. **Input/Output/Data (I/O/D):** (If applicable, e.g., for coding tasks)
    ◦ Expected input data/variables
    ◦ Expected output data/variables/side effects
10. **Development Steps:**
    1. Step-by-step instructions for the AI agent.
    2. (e.g., "1. Read the input schema from `automation_entities.md` for `TranscriptionTeam`.")
    3. (e.g., "2. Implement the main function in `src/teams/transcription_team.py`.")
    4. (e.g., "3. Ensure error handling for API call failures.")
    5. (e.g., "4. Run the test defined in `Tests/Task_1_Test_1.md`.")
11. **Dependencies:** (List of Task IDs that must be completed first)
12. **Estimated Effort:** (Optional points/time)
**`Project_Name/Sprint_N/Tests/Task_X_Test_Y.md`**
*Purpose: Describes a specific test case associated with a task.*
1. **Test ID:** (e.g., `S1_Test_T1_1`)
2. **Associated Task ID:** (The task this test verifies, e.g., `S1_T2`)
3. **Task ID (Test Creation):** (The task responsible for *writing* this test code, e.g., `S1_T1`)
4. **Summary:** (Matches summary in `tests.json`)
5. **Description:** Explanation of the test's purpose and what it aims to verify.
6. **Use Cases / Scenarios:**
    ◦ **Scenario 1:** Basic valid input
        ▪ Input Data: (Description or path to test data)
        ▪ Expected Outcome: (Description of expected output, state change, or behavior)
    ◦ **Scenario 2:** Edge case (e.g., empty input)
        ▪ Input Data: ...
        ▪ Expected Outcome: (e.g., Graceful error handling, specific error message)
    ◦ **Scenario 3:** ...
7. **Test Type:** (Unit, Integration, E2E, Evaluation)
8. **Manual Steps:** (If any required, describe precisely)
9. **Dependencies:** (Other tests that must pass first, or setup required)

##