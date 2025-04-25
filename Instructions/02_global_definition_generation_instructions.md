# Instructions: Global Project Definition Generation

**Note:** Assumes Current Working Directory (CWD) is the specific project root (e.g., `/Users/federicolopez/Automated_R100/My_Project1/`). Paths are relative to this CWD.

**Goal:** Generate the core definition files for the project based on the PRD.

**Trigger:** Completion of `project_prd.md`.

**Input:**
- `project_prd.md`
- Relevant guidelines from `../System_Memory_Bank/` (e.g., ontology definitions, entity patterns).
- Optional: Human-provided structure definition (if available).

**Steps:**
1.  **Read PRD:** Analyze the requirements outlined in `project_prd.md`.
2.  **Consult System Memory:** Refer to `../System_Memory_Bank` files for standard patterns and guidelines on defining ontologies, automation entities, state management, and DoD checklists.
3.  **Define Ontology:** Based on the PRD and guidelines, identify and define key project concepts, entities, and their relationships. Write this to `project_ontology.md`.
4.  **Define Automation Entities:** Identify potential Teams, Tools, Containers, and Events needed to fulfill the requirements. Create high-level summaries (I/O/D) in `automation_entities_summary.md` and detailed specifications in `automation_entities.md`.
5.  **Define State Management:** Based on the defined entities and ontology, establish rules for state variable handling. Write these to `state_manager_instructions.md`.
6.  **Define DoD Checklist:** Create a project-specific Definition of Done checklist, potentially extending a base checklist from `../System_Memory_Bank/reference_dod.md`. Write this to `definition_of_done_checklist.md`.
7.  **Update Context:** Update `activeContext.md` to reflect the completion of this stage and indicate that project planning is the next step.

**Output:**
- `project_ontology.md` created/updated.
- `automation_entities_summary.md` created/updated.
- `automation_entities.md` created/updated.
- `state_manager_instructions.md` created/updated.
- `definition_of_done_checklist.md` created/updated.
- `activeContext.md` updated.

**Next Workflow:** Project Planning (Sprint Generation)
