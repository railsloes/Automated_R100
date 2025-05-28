# {PROJECT_NAME} Directory Structure

This document outlines the standard directory structure and file naming conventions observed within the `{PROJECT_NAME}` project, managed by the Automated_R100 system. The structure organizes the project's code, documentation, sprint artifacts, and global definitions.

## Root Level (`{PROJECT_NAME}/`)

The root directory of the project, named `{PROJECT_NAME}`.

```
{PROJECT_NAME}/
├── Sprint_{SPRINT_NUMBER}/
├── src/
├── auxiliary/
├── activeContext.md
├── automation_entities.md
├── automation_entities_summary.md
├── definition_of_done_checklist.md
├── project_ontology.md
├── project_prd.md
├── sprints.json
├── state_manager_instructions.md
├── .gitignore
├── requirements.txt  (or equivalent dependency file)
└── README.md         (If generated/present)
```

*   **`Sprint_{SPRINT_NUMBER}/`**: Contains artifacts for a specific sprint. Numbering (`{SPRINT_NUMBER}`) starts from 1.
    *   `sprint_{SPRINT_NUMBER}_description.md`: Outlines the goals, scope, requirements, and Definition of Done (DoD) for the sprint.
    *   `tasks.json`: A JSON list of all tasks planned for the sprint, including their ID, description, type, and status (e.g., "Todo", "InProgress", "Done", "Blocked"). (Note: name seems to be `tasks.json`, not `sprint_{SPRINT_NUMBER}_tasks.json` based on observation).
    *   `tests.json`: A JSON list of tests associated with the sprint's tasks, including test ID, description, related task ID, and status (e.g., "Pending", "Pass", "Fail"). (Note: name seems to be `tests.json`, not `sprint_{SPRINT_NUMBER}_tests.json` based on observation).
    *   **`Tasks/`**: Contains detailed files for each task within the sprint.
        *   `task_{TASK_NUMBER}.md`: The primary description of the task, its goals, and requirements. (`{TASK_NUMBER}` is sequential within the sprint).
        *   `task_{TASK_NUMBER}_context.md`: Generated context summary relevant to the task, including focus areas, code pointers, history, etc.
        *   `task_{TASK_NUMBER}_function_dependencies.md`: Generated analysis of code dependencies relevant to the task, potentially with diagrams.
        *   `task_{TASK_NUMBER}_hypothesis.json`: A JSON list tracking hypotheses generated for the task, including their ID, statement, status (`pending`, `mentally_supported`, `code_supported`, `mentally_contradicted`, `code_contradicted`, etc.), and judgement.
        *   `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: Detailed breakdown of a specific hypothesis (`{HYPOTHESIS_NUMBER}` is sequential per task), including rationale, expected outcome, verification strategy, and analysis results (mental/code).
    *   **`Tests/`**: Contains automated tests specifically relevant to the tasks within this sprint. Test organization might mirror `src/` or be structured differently.
    *   **`Code/`**: (Optional) May contain sprint-specific code snippets or temporary files if needed, but primary code resides in `src/`.
*   **`src/`**: Contains the actual source code of the project, organized by features or modules.
    *   *(Subdirectories based on project architecture, e.g., `tools/`, `utils/`, `models/`, `routes/`, etc.)*
*   **`auxiliary/`**: Contains auxiliary files or resources supporting the project or automation process. (Contents to be detailed if known).
*   **`activeContext.md`**: Dynamically updated file reflecting the current state of the project, recent activities, errors, and next steps.
*   **`automation_entities.md`**: Lists the identified automation entities (Teams, Tools, Containers, Events) to be developed.
*   **`automation_entities_summary.md`**: A summary view of the automation entities.
*   **`definition_of_done_checklist.md`**: Checklist defining the criteria for task completion.
*   **`project_ontology.md`**: Defines the key concepts, entities, and relationships specific to the project domain.
*   **`project_prd.md`**: Project Product Requirements Document.
*   **`sprints.json`**: Defines the planned sprints for the project.
*   **`state_manager_instructions.md`**: Instructions related to state management.
*   **`.gitignore`**: Standard Git ignore file.
*   **`requirements.txt`** (or similar): Lists project dependencies (e.g., Python packages).
*   **`README.md`**: (If present) Project overview, setup instructions, etc.

## Naming Patterns

*   **Directories:** Use `PascalCase` or `snake_case`. Sprint directories are `Sprint_{SPRINT_NUMBER}`. `Tasks` and `Tests` within sprints use `PascalCase`.
*   **Files:** Generally use `snake_case`, except for `README.md`, `.gitignore`.
    *   Sprint-level files: `sprint_{SPRINT_NUMBER}_description.md`, `tasks.json`, `tests.json`.
    *   Task-level files: `task_{TASK_NUMBER}_*.ext`
    *   Hypothesis files: `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`
*   **Placeholders:**
    *   `{PROJECT_NAME}`: Replaced with the actual project name (`My_Project` in this case).
    *   `{SPRINT_NUMBER}`: Replaced with the specific sprint number (1, 2, ...).
    *   `{TASK_NUMBER}`: Replaced with the specific task number (1, 2, ...) within a sprint.
    *   `{HYPOTHESIS_NUMBER}`: Replaced with the specific hypothesis number (1, 2, ...) within a task.
    *   `{TEST_NUMBER}`: A reference placeholder used in documentation/hypotheses to link to a specific test case or scenario. The actual test function name in the code should be descriptive.

This structure reflects the current state of `{PROJECT_NAME}` and aims to promote consistency.