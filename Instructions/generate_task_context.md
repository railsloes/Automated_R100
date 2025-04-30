**Rule:** Generate Task Context Summary

**Goal:** To analyze the codebase relevant to a specific task  from the current sprint's task (e.g. task_1.md) and generate a markdown file, `task_{TASK_NUMBER}_context.md`, containing summaries, key information, and a narrative overview to aid understanding.

**Inputs:**

1.  `{TASK_GOAL}`: A natural language description of the development task
2.  `{CODEBASE_ROOT}`: The root directory of the project's codebase.
3.  (Optional) `{ERROR_LOG}`: Path to a relevant error log file, if applicable.

**Output:**

1.  `task_{TASK_NUMBER}_context.md`: A markdown file containing:
    * The original `{TASK_GOAL}`.
    * A list of identified "Focus Points" (relevant files/functions/classes).
    * Summaries of the purpose and behavior of key analyzed functions/classes.
    * Notes on relevant variable definitions/usage (where identifiable).
    * The error log (if provided).
    * Factual summary from `{ERROR_LOG}` (if provided). 
    * Summary of relevant commit history for Focus Point files.
    * A final human-readable narrative summarizing the context relevant to the `{TASK_GOAL}`.

**Execution Steps:**

**Phase 1: Initialization and Focus Point Identification**

1.  **Initialize File:** Create or clear the contents of `task_{TASK_NUMBER}_context.md`.
2.  **Record Task Goal:** Write the `{TASK_GOAL}` to the beginning of `task_{TASK_NUMBER}_context.md`.
3.  **Extract Keywords:** Analyze the `{TASK_GOAL}` to identify potential keywords (file names, function/class names, error messages, concepts).
4.  **Locate Initial Artifacts:** Search within `{CODEBASE_ROOT}` for files, functions, or classes matching the keywords.
5.  **Define Focus Points:**
    * Identify the top 3-5 most relevant matches based on the search and `{TASK_GOAL}`.
    * Record these as "Focus Points" in `task_{TASK_NUMBER}_context.md`. Example:
        ```markdown
        ## Focus Points
        * File: `src/auth.py`
        * Function: `process_data(data: dict)` in `src/core/processing.py`
        ```
6.  **Initialize Exploration Queue:** Create an internal queue and add all initial Focus Points to it. *This queue is used internally by this rule to guide analysis for context generation.*

**Phase 2: Iterative Analysis for Context**

**Loop:** While the Exploration Queue is not empty:

7.  **Select Next Item:** Dequeue an item (`CURRENT_ITEM`).
8.  **Relevance Check:** Briefly assess if `CURRENT_ITEM` seems relevant for providing context to the `{TASK_GOAL}`. If not, discard and continue loop.
9.  **Perform Analysis & Record Context (Write to `task_{TASK_NUMBER}_context.md`):**

    * **If `CURRENT_ITEM` is a file path:**
        * **a. Commit History:**
            * Execute `git log --follow -- <CURRENT_ITEM>` within `{CODEBASE_ROOT}`.
            * Analyze recent commit messages.
            * Write a brief summary in `task_{TASK_NUMBER}_context.md` under a "Commit Evolution Summary" section for this file, focusing on potentially relevant changes.
                ```markdown
                ### Commit Evolution Summary: `src/auth.py`
                * [Summary of recent relevant changes]
                ```
        * **b. Identify Key Components:** Analyze the file structure to identify key functions/classes within it that seem relevant to the task goal. Add these identified components (functions, classes) to the Exploration Queue if they haven't been processed.

    * **If `CURRENT_ITEM` is a function or method:**
        * **c. Code Retrieval:** Get the source code.
        * **d. Signature & Semantics:**
            * Analyze its signature, docstring, and body.
            * Write a concise summary of its purpose and behavior in `task_{TASK_NUMBER}_context.md` under a "Function/Method Analysis" section. Note key parameters, return values, or logic relevant to `{TASK_GOAL}`.
                ```markdown
                ### Function Analysis: `process_data(data: dict)` in `src/core/processing.py`
                * **Signature:** ...
                * **Purpose:** ... [Concise summary relevant to the task] ...
                ```
        * **e. Add Related Items:** Identify significant callees or related functions/methods directly relevant to understanding `CURRENT_ITEM`'s context for the task. Add these to the Exploration Queue if not processed. *Do not record the call graph here; that's for the other rule.*

    * **If `CURRENT_ITEM` is a class:**
        * **f. Analyze Definition:** Examine `__init__`, key methods, attributes, inheritance.
        * **g. Summarize Purpose:** Write a concise summary of the class's role relative to the `{TASK_GOAL}` in `task_{TASK_NUMBER}_context.md` under a "Class Analysis" section.
        * **h. Add Related Items:** Identify key methods within the class or related classes crucial for the task context. Add these to the Exploration Queue if not processed.

**End Loop**

**Phase 3: Finalization**

10. **Process Error Log (If applicable):**
    * If `{ERROR_LOG}` was provided:
        * Read the log file.
        * Extract factual error messages, stack traces, involved files/lines.
        * Write a factual summary into `task_{TASK_NUMBER}_context.md` under an "Error Summary" section.
            ```markdown
            ## Error Summary (`{ERROR_LOG}`)
            * **Error:** ...
            * **Location:** ...
            * **Trace Snippet:** ...
            ```
11. **Synthesize Narrative Summary:**
    * Based *only* on the information gathered *within this rule* and recorded in `task_{TASK_NUMBER}_context.md`:
        * Describe the purpose of the key components analyzed (focus points, relevant functions/classes).
        * Briefly mention relevant findings from commit history or error logs.
    * Write this narrative at the end of `task_{TASK_NUMBER}_context.md` under a "Context Narrative Summary" section.

**Completion:** The file `task_{TASK_NUMBER}_context.md` now contains the contextual summary documentation.

**Next Action:**  Execute `generate_task_function_dependencies.md`

