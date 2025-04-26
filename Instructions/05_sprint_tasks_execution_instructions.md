# Instructions: NEXT Sprint Tasks Execution

**Note:** 
- Assumes Current Working Directory (CWD) is the specific project root (e.g., `/Users/federicolopez/Automated_R100/{PROJECT_NAME}/`). Paths are relative to this CWD.
- Before starting, ensure that the previous task has been completed (status 'Done') or marked as 'Failed' or 'Cancelled'.
- Before starting, ensure that you have committed all changes.

**Goal:** Execute a specific, planned task from the current sprint's task list.

**Trigger:** A task in `Sprint_{SPRINT_NUMBER}/tasks.json` has status 'Todo' and all its dependencies (if any) have been met (status 'Done').

**Input (for Task_{TASK_NUMBER} in Sprint {SPRINT_NUMBER}):**
- `Sprint_{SPRINT_NUMBER}/Tasks/Task_{TASK_NUMBER}.md` (Primary instructions, steps, criteria)
- Relevant `Sprint_{SPRINT_NUMBER}/Tests/Task_{TASK_NUMBER}_Test_{TEST_NUMBER}.md` files (for context or execution)
- Existing code in `src/`
- `activeContext.md` (for recent state)
- Potentially: Generated data from `auxiliary/generated_data/`
- Potentially: `task_{TASK_NUMBER}_context.md`, `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` (for context of execution)

**Steps (General Execution Flow):**
1.  **Select Task:** Identify the next available task (`status: 'Todo'`, dependencies met) from `Sprint_{SPRINT_NUMBER}/tasks.json`.
2.  **Update Task Status :** 
Change the status of the selected task in `Sprint_{SPRINT_NUMBER}/tasks.json` to 'In Progress'. Update `activeContext.md` to reflect the currently active task.
Task status can be 'Todo', 'In Progress', 'Done', 'Failed' or 'Cancelled'.

3.  **Read Task Definition:** Thoroughly understand the requirements, steps, and acceptance criteria outlined in `Sprint_{SPRINT_NUMBER}/Tasks/Task_{TASK_NUMBER}.md`.
4.  **Execute Steps:** Perform the actions defined in the task's steps. This may involve:
    *   Writing or modifying code in `src/`.
    *   Running tests (using generated data if applicable).
    *   Generating data/files in `auxiliary/`.
    *   Writing documentation.
    *   Interacting with external systems (Git, databases, APIs).
    *   Consulting `System_Memory_Bank/Debugging.md` if issues arise.
    *   Avoid creating new directories, prefer to find existing ones or use the existing structure.
5.  **Verify Acceptance Criteria:** Ensure all acceptance criteria defined in `Task_{TASK_NUMBER}.md` are met.
6.  **Update Task Status (Final):** Change the status of the task in `Sprint_{SPRINT_NUMBER}/tasks.json` to 'Done'.
7.  **Update Test Status:** If the task involved running tests, update the status of corresponding tests in `Sprint_{SPRINT_NUMBER}/tests.json` (e.g., 'Pass' or 'Fail').
8.  **Update Context:** Update `activeContext.md` to reflect task completion, any significant outcomes, and readiness for the next task.
9.  **Handle Conditional Tasks:** If the completed task triggers conditional follow-up tasks (e.g., Definition Update, Replanning, Git operations specified during Task Generation), ensure these are added to `Sprint_{SPRINT_NUMBER}/tasks.json` with appropriate status and dependencies.
10. **Commit Changes:** If the task involved writing or modifying code, commit all changes to the `src/` directory. Include the task name and a brief description in the commit message.
11. **Push Changes at the End of a Sprint:** If the task involved finishing a Sprint, push all changes.

**Output (Variable depending on Task Type):**
- Modified/new code files in `src/`.
- Updated status in `Sprint_{SPRINT_NUMBER}/tasks.json` and potentially `Sprint_{SPRINT_NUMBER}/tests.json`.
- Updated `activeContext.md`.
- Files created in `auxiliary/` (e.g., logs, generated data).
- External interactions logged or completed (e.g., Git commit/push, DB record update).
- Potentially new tasks added to `Sprint_{SPRINT_NUMBER}/tasks.json`.

**Next Action if Task is Done:** Select the next available task from `Sprint_{SPRINT_NUMBER}/tasks.json`.
**Next Action if Task Failed:** 
-Review if  `task_{TASK_NUMBER}_context.md` exists, if not, execute `generate_task_context.md`.
-Review if  `task_{TASK_NUMBER}_function_dependencies.md` exists, if not, execute `generate_task_function_dependencies.md`.
-Review if  `task_{TASK_NUMBER}_hypothesis.json` exists, if not, execute `generate_task_hypothesis.md`.
-Review `task_{TASK_NUMBER}_hypothesis.json`and execute `analyze_hypothesis_mentally.md` or `analyze_hypothesis_code.md` to try to execute the task or create a new hypothesis with `generate_task_hypothesis.md` if the hypothesis is not valid either mentally or by code analysis.
