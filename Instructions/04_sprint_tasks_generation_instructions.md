# Instructions: NEXT Sprint Tasks Generation

**Note:** Assumes Current Working Directory (CWD) is the specific project root (e.g., `/Users/federicolopez/Automated_R100/My_Project1/`). Paths are relative to this CWD.

**Goal:** Generate detailed, actionable tasks and corresponding test definitions for the upcoming sprint based on its goals and the planned automation entities.

**Trigger:** Completion of `Sprint_N/sprint_description.md` for the sprint being planned.

**Common Inputs (for Sprint N):**
- `Sprint_N/sprint_description.md`
- `automation_entities.md` (for entities scheduled in Sprint N)
- `project_ontology.md`
- Relevant files from `System_Memory_Bank/` (e.g., `Teams.md`, `Tools.md`, `Containers.md`, `Events.md`, `testing_definition.md`, `deployment_pattern.md`)

**Common Outputs (for Sprint N):**
- Entries added to `Sprint_N/tasks.json` (status 'Todo', type specified).
- Entries added to `Sprint_N/tests.json` (status 'Pending').
- Detailed Task definition files created in `Sprint_N/Tasks/Task_*.md`.
- Detailed Test definition files created in `Sprint_N/Tests/Task_*_Test_*.md`.
- `activeContext.md` updated (reflecting task generation completion, next step is task execution).

**Process (Executed per Entity Type scheduled in the Sprint):**

**1. Generate Tasks for Teams:**
   - **Inputs:** `System_Memory_Bank/Teams.md`, `System_Memory_Bank/deployment_pattern.md`.
   - **Steps:**
     1. Identify Teams for this sprint.
     2. Consult `System_Memory_Bank/Teams.md` for patterns.
     3. Create Test Tasks (`task_type: Testing`) to *write* test code (unit, integration) first. Create corresponding `Sprint_N/Tests/Task_*_Test_*.md` and `Sprint_N/tests.json` entries.
     4. Create Coding Tasks (`task_type: Coding`) to *implement* Team logic (Execution Team first, then Evaluation if applicable). Reference tests in `Sprint_N/Tasks/Task_*.md`.
     5. Create Documentation Task (`task_type: Documentation`).
     6. Create Data Generation Task (`task_type: Data Generation`) for test/DoD data (specify storage, e.g., `auxiliary/generated_data/`).
     7. *Conditional:* Create Project Test Execution Task (`task_type: Testing`) to run *all* relevant project tests if Team is 'complete' in sprint context.
     8. Create Deployment Task (`task_type: Deployment`) to register Team (ref `System_Memory_Bank/deployment_pattern.md`).
     9. Create standard Update & Git Tasks (`task_type: Update Context`, `task_type: Git`).
     10. *Conditional:* Create Definition Update Tasks if I/O/D change significantly (`automation_*.md`, `project_ontology.md`, `state_manager_instructions.md`).
     11. *Conditional:* Create Replanning Task (`task_type: Workflow`, sub_type: Replanning) if core I/O/D changes significantly.

**2. Generate Tasks for Tools (Container & Internal):**
   - **Inputs:** `System_Memory_Bank/Tools.md`.
   - **Steps:**
     1. Identify Tools for this sprint.
     2. Consult `System_Memory_Bank/Tools.md`.
     3. Create Test Tasks (`task_type: Testing`) to write tests. Create `Sprint_N/Tests/Task_*_Test_*.md` and `Sprint_N/tests.json` entries.
     4. Create Coding Tasks (`task_type: Coding`). Query host assistant if needed.
     5. Create Data Generation Task (`task_type: Data Generation`).
     6. Create Local Test Execution Task (`task_type: Testing`).
     7. *Conditional:* Create Deployment/Update Task (`task_type: Deployment`) for shared/online Tools.
     8. *Conditional:* Create Online Test Execution Task (`task_type: Testing`) if deployed.
     9. Create Documentation Task (`task_type: Documentation`).
     10. Create standard Update & Git Tasks.
     11. *Conditional:* Create Definition Update Tasks if I/O/D change.
     12. *Conditional:* Create Replanning Task if I/O/D changes significantly.

**3. Generate Tasks for Containers:**
   - **Inputs:** `System_Memory_Bank/Containers.md`.
   - **Steps:**
     1. Identify Containers for this sprint.
     2. Consult `System_Memory_Bank/Containers.md`.
     3. Create Test Tasks (`task_type: Testing`) for integration tests (flow, variables). Create `Sprint_N/Tests/Task_*_Test_*.md` and `Sprint_N/tests.json` entries.
     4. Create Coding/Configuration Tasks (`task_type: Coding`) to define the Container (YAML/JSON/Script).
     5. Create Documentation Task (`task_type: Documentation`).
     6. Create Integration Test Execution Task (`task_type: Testing`).
     7. *Conditional:* Create Deployment Task (`task_type: Deployment`) if needed.
     8. Create standard Update & Git Tasks.
     9. *Conditional:* Create Definition Update Tasks if structure/logic changes significantly.
     10. *Conditional:* Create Replanning Task if structure/logic deviates significantly.

**4. Generate Tasks for Events:**
   - **Inputs:** `System_Memory_Bank/Events.md`.
   - **Steps:**
     1. Identify Event Handlers for this sprint.
     2. Consult `System_Memory_Bank/Events.md`.
     3. Create Data Generation Task (`task_type: Data Generation`) for sample event payloads.
     4. Create Test Tasks (`task_type: Testing`) for parsing/validation (may include manual steps). Create `Sprint_N/Tests/Task_*_Test_*.md` and `Sprint_N/tests.json` entries.
     5. Create Coding Tasks (`task_type: Coding`) to implement handler logic.
     6. Create Documentation Task (`task_type: Documentation`).
     7. Create Test Execution Task (`task_type: Testing`) (run automated, log manual).
     8. Create standard Update & Git Tasks.
     9. *Conditional:* Create Definition Update Tasks if schema/logic changes.
     10. *Conditional:* Create Replanning Task if schema/logic changes significantly.

**Next Workflow:** NEXT Sprint Tasks Execution
