# Instructions: NEXT Sprint Tasks Execution

**Note:** 
- Assumes Current Working Directory (CWD) is the specific project root (e.g., `/Users/federicolopez/Automated_R100/My_Project1/`). Paths are relative to this CWD.
- Before starting, ensure that the previous task has been completed (status 'Done') or marked as 'Failed' or 'Cancelled'.
- Before starting, ensure that you have committed all changes.

**Goal:** Execute a specific, planned task from the current sprint's task list.

**Trigger:** A task in `Sprint_N/tasks.json` has status 'Todo' and all its dependencies (if any) have been met (status 'Done').

**Input (for Task X in Sprint N):**
- `Sprint_N/Tasks/Task_X.md` (Primary instructions, steps, criteria)
- Relevant `Sprint_N/Tests/Task_*_Test_*.md` files (for context or execution)
- Existing code in `src/`
- `System_Memory_Bank/Debugging.md` (if errors occur)
- `activeContext.md` (for recent state)
- Potentially: Generated data from `auxiliary/generated_data/`

**Steps (General Execution Flow):**
1.  **Select Task:** Identify the next available task (`status: 'Todo'`, dependencies met) from `Sprint_N/tasks.json`.
2.  **Update Task Status :** 
Change the status of the selected task in `Sprint_N/tasks.json` to 'In Progress'. Update `activeContext.md` to reflect the currently active task.
Task status can be 'Todo', 'In Progress', 'Done', 'Failed' or 'Cancelled'.

3.  **Read Task Definition:** Thoroughly understand the requirements, steps, and acceptance criteria outlined in `Sprint_N/Tasks/Task_X.md`.
4.  **Execute Steps:** Perform the actions defined in the task's steps. This may involve:
    *   Writing or modifying code in `src/`.
    *   Running tests (using generated data if applicable).
    *   Generating data/files in `auxiliary/`.
    *   Writing documentation.
    *   Interacting with external systems (Git, databases, APIs).
    *   Consulting `System_Memory_Bank/Debugging.md` if issues arise.
    *   Avoid creating new directories, prefer to find existing ones or use the existing structure.
5.  **Verify Acceptance Criteria:** Ensure all acceptance criteria defined in `Task_X.md` are met.
6.  **Update Task Status (Final):** Change the status of the task in `Sprint_N/tasks.json` to 'Done'.
7.  **Update Test Status:** If the task involved running tests, update the status of corresponding tests in `Sprint_N/tests.json` (e.g., 'Pass' or 'Fail').
8.  **Update Context:** Update `activeContext.md` to reflect task completion, any significant outcomes, and readiness for the next task.
9.  **Handle Conditional Tasks:** If the completed task triggers conditional follow-up tasks (e.g., Definition Update, Replanning, Git operations specified during Task Generation), ensure these are added to `Sprint_N/tasks.json` with appropriate status and dependencies.
10. **Commit Changes:** If the task involved writing or modifying code, commit all changes to the `src/` directory.
11. **Push Changes at the End of a Sprint:** If the task involved finishing a Sprint, push all changes.

**Output (Variable depending on Task Type):**
- Modified/new code files in `src/`.
- Updated status in `Sprint_N/tasks.json` and potentially `Sprint_N/tests.json`.
- Updated `activeContext.md`.
- Files created in `auxiliary/` (e.g., logs, generated data).
- External interactions logged or completed (e.g., Git commit/push, DB record update).
- Potentially new tasks added to `Sprint_N/tasks.json`.

**Next Action:** Select the next available task from `Sprint_N/tasks.json`.
