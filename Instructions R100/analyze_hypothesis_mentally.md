**Rule: Analyze Hypothesis Mentally**

**Goal:** To perform a preliminary, non-execution-based evaluation of a specific hypothesis using static analysis, simulated execution concepts, contextual checks, and counterfactual reasoning to assess its validity and guide subsequent actions.

**Inputs:**

1.  `{TASK_GOAL}`: The original natural language description of the development task.
2.  `{TASK_NUMBER}`: The numerical identifier for the current task.
3.  `{HYPOTHESIS_NUMBER}`: The numerical identifier for the specific hypothesis being analyzed.
4.  `task_{TASK_NUMBER}.md`: The main task description file.
5.  `task_{TASK_NUMBER}_context.md`: File containing context summaries, focus points, etc.
6.  `task_{TASK_NUMBER}_function_dependencies.md`: File detailing function/module dependencies.
7.  `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: The specific hypothesis detail file to be analyzed.
8.  `task_{TASK_NUMBER}_hypothesis.json`: The JSON file containing the list of all hypotheses for the task.

**Outputs:**

1.  `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: The **updated** hypothesis detail file with a new section appended, containing the "Mental Analysis Results".
2.  `task_{TASK_NUMBER}_hypothesis.json`: The **updated** JSON file where the `status` and the `judgement` of the analyzed hypothesis (`hypothesis_id: "Hypothesis_{HYPOTHESIS_NUMBER}"`) is updated based on the mental analysis outcome.

**Execution Steps:**

**Phase 1: Preparation**

1.  **Load Inputs:** Read and parse the content from all input files, paying close attention to the specific hypothesis details in `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`.

**Phase 2: Mental Analysis**

2.  **Static Analysis & Code Review:**
    * Examine the code locations identified in `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`.
    * Check for syntactic correctness, type consistency (based on hints or inference), and potential linting issues relevant to the hypothesis.
    * Assess the plausibility of the hypothesized behavior based on variable names, comments, and local code structure.
    * Look for known anti-patterns or vulnerabilities related to the hypothesis statement.
    * *Record findings relevant to supporting or contradicting the hypothesis.*

3.  **Simulated Execution / Symbolic Analysis (Conceptual):**
    * Mentally trace or simulate the execution path(s) relevant to the hypothesis, starting from the triggering conditions specified in `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` (Section 4).
    * Track the state of key variables identified in Section 6 during this simulated trace.
    * (Advanced) If possible, apply symbolic reasoning: Assume symbolic values based on the triggering condition and track constraints. Can the symbolic state reach the outcome predicted by the hypothesis?
    * Compare the simulated/symbolic outcome with the "Expected Outcome" (Section 7) in the hypothesis file.
    * *Record findings: Does the simulation align with, contradict, or remain inconclusive regarding the hypothesis?*

4.  **Contextual Consistency Check:**
    * Compare the hypothesis statement and its implications against the broader context in `task_{TASK_NUMBER}_context.md` and `task_{TASK_NUMBER}_function_dependencies.md`.
    * Check for contradictions: Does the hypothesis violate known module dependencies? Does it conflict with the documented purpose of involved functions? Is it inconsistent with recent relevant changes noted in commit history summaries?
    * *Record findings: Is the hypothesis consistent with the overall system understanding?*

5.  **Counterfactual Reasoning (Conceptual):**
    * Briefly consider simple counterfactuals. If the triggering condition (Section 4) were slightly different (e.g., `user_status='premium'` instead of `'guest'`), would the hypothesized outcome still occur according to the code logic?
    * Does the hypothesis explain why alternative conditions *don't* lead to the outcome (if applicable)?
    * *Record findings: Does the hypothesis hold up under minor variations, increasing confidence?*

**Phase 3: Synthesis and Output**

6.  **Synthesize Evaluation Outcome:**
    * Consolidate all findings from steps 2-5.
    * Determine the level of confidence:
        * **Mentally Supported:** Evidence from analysis consistently aligns with the hypothesis.
        * **Mentally Contradicted:** Clear evidence contradicts the hypothesis.
        * **Mentally Uncertain:** Analysis is inconclusive; ambiguities or missing information prevent a clear judgment.
    * Generate a judgement paragraph explaining the reasoning for the determined confidence level, citing specific evidence from the analysis steps.

7.  **Update Hypothesis Detail File (`task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`):**
    * Append a new section to the end of the file:
        ```markdown
        ---

        **9. Mental Analysis Results:**

        * **Confidence Level:** [Mentally Supported | Mentally Contradicted | Mentally Uncertain]
        * **Judgement:** [Insert the summary paragraph generated in Step 6 here. Explain the evidence found during static analysis, simulation, contextual checks, etc.]
        * **Recommendation:** [Suggest next step based on confidence level, e.g., "Proceed to code-based evaluation.", "Reject hypothesis.", "Needs further investigation into X before proceeding."]
        ```

8.  **Update Hypothesis JSON (`task_{TASK_NUMBER}_hypothesis.json`):**
    * Read the existing JSON content.
    * Find the JSON object where `hypothesis_id` matches `Hypothesis_{HYPOTHESIS_NUMBER}`.
    * Update the `status` field for that object to reflect the outcome (e.g., `"status": "mentally_supported"`, `"status": "mentally_contradicted"`, `"status": "mentally_uncertain"`) and the `judgement` field with the judgement paragraph generated in Step 6.
    * Write the updated list back to `task_{TASK_NUMBER}_hypothesis.json`.

**Completion:** The hypothesis detail file (`task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`) is updated with the mental analysis results and recommendation. The overall hypothesis list (`task_{TASK_NUMBER}_hypothesis.json`) reflects the updated status.

