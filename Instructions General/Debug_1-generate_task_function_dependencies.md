---

**Instruction File 2: `generate_task_function_dependencies.md`**

**Rule:** Generate Task Function/Module Dependencies

**Goal:** To analyze the codebase relevant to a specific task and generate a markdown file, `task_{TASK_NUMBER}_function_dependencies.md`, detailing the relevant import, call, and usage relationships between modules, functions, and classes.

**Inputs:**
READ_FROM_FILE(task_{TASK_NUMBER}_context.md) and get TASK_GOAL, CODEBASE_ROOT, and FOCUS_POINTS_LIST.
1.  `{TASK_GOAL}`: A natural language description of the development task (must be the same as used for `generate_task_context.md`).
2.  `{CODEBASE_ROOT}`: The root directory of the project's codebase.
3.  (Optional) `{FOCUS_POINTS_LIST}`: A pre-defined list of starting focus points (file paths, function/class signatures). If not provided, they will be derived from `{TASK_GOAL}` as in Phase 1 below. 

**Output:**

1.  `task_{TASK_NUMBER}_function_dependencies.md`: A markdown file outlining the hierarchical dependencies (imports/exports, calls, usage) between analyzed modules, functions, and classes relevant to the `{TASK_GOAL}`.

**Execution Steps:**

**Phase 1: Initialization and Focus Point Identification**

1.  **Initialize File:** Create or clear the contents of `task_{TASK_NUMBER}_function_dependencies.md`.
2.  **Determine Focus Points:**
    * If `{FOCUS_POINTS_LIST}` is provided, use it as the initial set of Focus Points.
    * If `{FOCUS_POINTS_LIST}` is *not* provided:
        * Extract Keywords: Analyze the `{TASK_GOAL}` for keywords.
        * Locate Initial Artifacts: Search within `{CODEBASE_ROOT}` for matches.
        * Define Focus Points: Identify the top 3-5 most relevant matches.
3.  **Initialize Exploration Queue:** Create an internal queue and add all Focus Points to it. *This queue guides the dependency analysis.*

**Phase 2: Iterative Analysis for Dependencies**

**Loop:** While the Exploration Queue is not empty:

4.  **Select Next Item:** Dequeue an item (`CURRENT_ITEM`).
5.  **Relevance Check:** Briefly assess if analyzing the dependencies of `CURRENT_ITEM` is relevant to the `{TASK_GOAL}`. If not, discard and continue loop.
6.  **Perform Analysis & Record Dependencies (Write to `task_{TASK_NUMBER}_function_dependencies.md`):**

    * **If `CURRENT_ITEM` is a file path:**
        * **a. Module Dependencies:**
            * Analyze the file's import statements. List modules/files it imports.
            * Search the codebase for modules/files that import this file.
            * Record these import/imported-by relationships in `task_{TASK_NUMBER}_function_dependencies.md` under a heading for the file path. Mark dependencies potentially relevant to the `{TASK_GOAL}`.
                ```markdown
                ### File: `src/auth.py`
                * **Imports:**
                    * `src/db/database.py` (Relevant)
                    * `src/utils/helpers.py`
                * **Imported By:**
                    * `src/server.py` (Relevant)
                ```
            * Add the *relevant* related files/modules to the Exploration Queue if not already processed or queued.

    * **If `CURRENT_ITEM` is a function or method:**
        * **b. Internal Calls (Callees):**
            * Identify significant function calls or class instantiations *within* its body.
            * List these callees in `task_{TASK_NUMBER}_function_dependencies.md` under the entry for `CURRENT_ITEM`. Mark relevance.
                ```markdown
                ### Function: `process_data(data: dict)` in `src/core/processing.py`
                * **Calls:**
                    * `validate_schema(data)` in `src/utils/validation.py` (Relevant)
                    * `db.save_record(processed_data)` in `src/db/database.py` (Relevant)
                ```
            * Add callees marked *Relevant* to the Exploration Queue if not processed/queued.
        * **c. External Calls (Callers):**
            * Search the codebase to find where `CURRENT_ITEM` is called from.
            * Summarize the calling context (where/why it's used) in `task_{TASK_NUMBER}_function_dependencies.md`. Mark relevance.
                ```markdown
                ### Function: `process_data(data: dict)` in `src/core/processing.py`
                * **Called By:**
                    * `handle_request(request)` in `src/server.py`: [Context snippet] (Relevant)
                ```
            * Add callers marked *Relevant* to the Exploration Queue if not processed/queued.

    * **If `CURRENT_ITEM` is a class:**
        * **d. Record Dependencies:** Analyze and record key relationships like inheritance, composition (attributes holding instances of other relevant classes), and significant external usage patterns (where it's instantiated or its methods are called). Structure this under a heading for the class in `task_{TASK_NUMBER}_function_dependencies.md`.
        * **e. Add Related Items:** Add relevant related classes, methods, or modules identified through these dependencies to the Exploration Queue.

**End Loop**

**Phase 3: Finalization**

7.  **Review and Structure:** Ensure the `task_ {TASK_NUMBER}_function_dependencies.md` file is well-structured, clearly showing the relationships discovered during the analysis loop. (No narrative summary is generated in this rule).

**Completion:** The file `task_{TASK_NUMBER}_function_dependencies.md` now contains the dependency graph documentation relevant to the task.
