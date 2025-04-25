# Instructions: Project Planning (Sprint Generation)

**Note:** Assumes Current Working Directory (CWD) is the specific project root (e.g., `/Users/federicolopez/Automated_R100/My_Project1/`). Paths are relative to this CWD.

**Goal:** Break down the project into logical Sprints and generate the plan.

**Trigger:** Completion of Global Project Definition files.

**Input:**
- `project_prd.md`
- `automation_entities.md`
- `definition_of_done_checklist.md`
- `state_manager_instructions.md`
- `project_ontology.md`
- Relevant planning patterns from `../System_Memory_Bank/`
- Optional: Information on existing reusable Teams/Tools (from host assistant/vector DB/developer input).

**Steps:**
1.  **Analyze Definitions:** Review the requirements (PRD) and the defined automation entities, including their dependencies (`automation_entities.md`).
2.  **Identify Reusables (Optional):** Check for existing Teams/Tools that can be reused, based on descriptions in `automation_entities.md` and external information/developer guidance.
3.  **Determine Sprint Structure:** Group the automation entities into logical Sprints based on dependencies and project goals. Consider reusable components when planning.
4.  **Generate Sprint Plan:** Create the overall sprint list and their initial status. Write this to `sprints.json`.
5.  **Generate Sprint Descriptions:** For each planned sprint (at least the first one), create the corresponding directory (e.g., `Sprint_1/`) and write a `sprint_description.md` file outlining the sprint's goals, scope, requirements, and specific DoD items.
6.  **Update Context:** Update `activeContext.md` to reflect the completion of planning and indicate that Task Generation for Sprint 1 is the next step.

**Output:**
- `sprints.json` created/updated.
- `Sprint_N/sprint_description.md` created for each planned sprint (at least Sprint 1).
- Sprint directories (`Sprint_N/`) created.
- `activeContext.md` updated.

**Next Workflow:** NEXT Sprint Tasks Generation
