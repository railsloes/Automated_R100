**Rule: Generate Task Hypothesis**

**Goal:** To analyze the gathered context and dependency information, perform structured reasoning (Rubber Duck Analysis), formulate specific, testable hypotheses about the code's behavior or required implementation steps relevant to the task, rank them, and output the top hypothesis in a structured format.

**Inputs:**

1.  `{TASK_GOAL}`: The original natural language description of the development task.
2.  `{TASK_NUMBER}`: The numerical identifier for the current task.
3.  `task_{TASK_NUMBER}.md`: The main task description file (referenced for overall goal).
4.  `task_{TASK_NUMBER}_context.md`: File containing context summaries, focus points, commit history, error summaries, etc.
5.  `task_{TASK_NUMBER}_function_dependencies.md`: File detailing function/module dependencies, call graphs, etc.
6.  `task_{TASK_NUMBER}_hypothesis.json`: A JSON file containing a list of previously generated/evaluated hypotheses for this task (can be empty or inexistent initially). Format: `[{"hypothesis_id": "...", "statement": "...", "status": "pending/tested_true/tested_false"}, {"judgement": "..."}]`.

**Outputs:**

1.  `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: A new markdown file (where {HYPOTHESIS_NUMBER} is the next sequential hypothesis number for this task, e.g., `task_{TASK_NUMBER}_hypothesis_1.md`, `task_{TASK_NUMBER}_hypothesis_2.md`) detailing the top-ranked, newly generated hypothesis in a structured format.
2.  `task_{TASK_NUMBER}_hypothesis.json`: Updated JSON file with the new hypothesis added (marked with `status: "pending"`).

**Execution Steps:**

**Phase 1: Input Analysis & Rubber Ducking**

1.  **Load Inputs:** Read and parse the content from `task_{TASK_NUMBER}.md`, `task_{TASK_NUMBER}_context.md`, `task_{TASK_NUMBER}_function_dependencies.md`, and `task_{TASK_NUMBER}_hypothesis.json`.
2.  **Perform Rubber Duck Analysis (Internal Reasoning Log):** Generate a structured internal articulation (this doesn't need to be saved to a file unless explicitly requested for debugging the process itself) covering:
    * **Re-state Goal:** "Current objective: [State the specific goal from `{TASK_GOAL}` clearly]."
    * **Summarize Key Context:** "Relevant context: [List key findings from `task_{TASK_NUMBER}_context.md` and `task_{TASK_NUMBER}_function_dependencies.md` - e.g., involved functions, critical dependencies, error details, relevant commit notes]."
    * **List Prior Hypotheses:** "Prior hypotheses status (from `task_{TASK_NUMBER}_hypothesis.json`): [Summarize previous hypotheses and their status, especially rejected ones and the reason for rejection]."
    * **Verbalize Sticking Point:** "Current reasoning impasse: [Describe the specific difficulty - e.g., 'uncertainty about data flow between function A and B', 'root cause of error X not pinpointed', 'best integration point for feature Y unclear']."
    * **Expose Assumptions:** "Current assumptions: [List explicit assumptions being made - e.g., 'assuming `get_data()` handles nulls', 'assuming config setting Z is enabled', 'external API call is reliable']."
    * **Logical Step-Through:** "Reviewing logic: [Step-by-step trace of how the context/dependencies lead to the current understanding or the sticking point]."
    * **Identify Gaps/Conflicts:** Based on the above, explicitly note any identified flawed assumptions, logical gaps, misinterpreted context, or conflicting information.

**Phase 2: Hypothesis Formulation & Ranking**

3.  **Identify Potential Causes / Implementation Paths:** Based on the Rubber Duck Analysis and the input files:
    * **(Debugging):** Brainstorm potential root causes for errors, informed by context (error messages, stack traces, dependencies, recent changes).
    * **(Implementation):** Identify candidate functions/classes for modification, suitable design patterns, and potential integration points, considering dependencies and architectural constraints. Predict potential impacts.
4.  **Formulate Specific, Testable Hypotheses:** Translate the potential causes/paths into 1-3 concrete, falsifiable statements. Each hypothesis should describe a specific mechanism or implementation choice.
5.  **Rank Hypotheses:** Evaluate the generated hypotheses based on factors like:
    * **Simplicity:** Is it the simplest explanation/approach?
    * **Evidence Fit:** How well does it align with `task_{TASK_NUMBER}_context.md` and `task_{TASK_NUMBER}_function_dependencies.md`?
    * **Likelihood/Plausibility:** Is this a common pattern or a likely scenario?
    * **Recency (for bugs):** Does it relate to recent changes noted in commit history?
    * **Testability:** How easily can this hypothesis be tested (e.g., via logging or specific tests)?
    * Assign a rank or score to each hypothesis. Select the top-ranked hypothesis.

**Phase 3: Output Generation**

6.  **Determine Next Hypothesis ID:** Check `task_{TASK_NUMBER}_hypothesis.json` to find the highest existing hypothesis number (N-1) for this task and set the new ID to N. If the file is empty or doesn't exist, start with N=1. Let the new ID be `Hypothesis_{HYPOTHESIS_NUMBER}`.
7.  **Create Hypothesis Detail File (`task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`):** Generate a new file named `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` with the following structure, filling in details for the **top-ranked** hypothesis:

    ```markdown
    # Hypothesis Detail: Hypothesis_{HYPOTHESIS_NUMBER}

    **1. Hypothesis ID:**
    Hypothesis_{HYPOTHESIS_NUMBER}

    **2. Source Task:**
    task_{TASK_NUMBER}.md (or reference to `{TASK_GOAL}`)

    **3. Hypothesis Statement:**
    [Insert the clear, concise statement of the top-ranked hypothesis here.]

    **4. Rationale / Triggering Condition:**
    [Explain why this hypothesis is proposed, referencing specific context from `task_{TASK_NUMBER}_context.md`, dependencies from `task_{TASK_NUMBER}_function_dependencies.md`, error messages, or logical deductions from the Rubber Duck Analysis. State conditions under which it's expected.]

    **5. Key Code Locations for Logging/Verification:**
    [List specific files, functions/methods, and approximate line numbers critical for observing the behavior related to this hypothesis.]
    * `path/to/file1.py`: `function_a` (around line X)
    * `path/to/file2.py`: `ClassName.method_b` (entry/exit)

    **6. Key Variables / State to Observe:**
    [Identify specific variables, parameters, or object attributes whose state needs to be checked or logged at the locations above.]
    * In `function_a`: variable `var1`, parameter `input_data`
    * In `method_b`: return value, attribute `self.status`

    **7. Expected Outcome (Confirmation Criteria):**
    [Describe the specific observation (e.g., log output pattern, variable value, state change) that would confirm this hypothesis.]
    * Example: "Logs should show `function_a` receiving `input_data` as None, and subsequently `method_b` returning `False`."

    **8. Suggested Test Case(s) (Optional):**
    [Suggest specific existing test cases (e.g., pytest `test_{TEST_NUMBER}`) or describe a new test scenario that could trigger the condition and verify the hypothesis.]
    * Example: `tests/test_module.py::test_function_a_with_null_input`
    ```

8.  **Update Hypothesis JSON (`task_{TASK_NUMBER}_hypothesis.json`):**
    * Read the existing JSON content.
    * Append a new JSON object for the generated hypothesis:
        ```json
        {
          "hypothesis_id": "Hypothesis_{HYPOTHESIS_NUMBER}",
          "statement": "[Insert the Hypothesis Statement from step 7]",
          "status": "pending",
          "judgement": ""
        }
        ```
    * Write the updated list back to `task_{TASK_NUMBER}_hypothesis.json`.

**Completion:** The file `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` is created with the details of the top hypothesis, and `task_{TASK_NUMBER}_hypothesis.json` is updated.

---

**Sample Output Content (`task_{TASK_NUMBER}_hypothesis_1.md` - Initial Generation):**

```markdown
# Hypothesis Detail: Hypothesis_1

**1. Hypothesis ID:**
Hypothesis_1

**2. Source Task:**
task_{TASK_NUMBER}.md (Refactor auth flow to JWT)

**3. Hypothesis Statement:**
The primary modification needed for the `/login` endpoint in `src/routes/auth.py` is to replace the call to `utils.session_manager.create_session` with a call to a new function `utils.jwt_handler.create_access_token`...

**4. Rationale:**
Based on the goal to move away from sessions and the dependency analysis showing `routes.auth.login_user` calling `session_manager.create_session`...

**5. Key Code Locations/Variables:**
*   File: `src/routes/auth.py`
*   Function: `login_user`
*   Call to replace: `utils.session_manager.create_session(...)`
*   Call to add: `utils.jwt_handler.create_access_token(user_id=...)`

**6. Expected Outcome (If True):**
Modifying the `/login` endpoint as described will allow a user to receive a JWT upon successful login...

**7. Potential Side Effects:**
*   Existing session-based checks will fail.
*   Requires creation of `utils.jwt_handler.py`.

**8. Verification Strategy (Mental/Code):**
*   **Mental:** Trace the `/login` flow...
*   **Code:** Implement change and write test for `/login` (e.g., `test_{TEST_NUMBER}` in `tests/test_auth.py`)...

**--- Analysis Sections (To be filled by later steps) ---**

**9. Mental Analysis Result:**
*   **Status:** Pending

**10. Code Analysis Result:**
*   **Status:** Pending
