**Rule: Analyze Hypothesis with Code**

**Goal:** To evaluate a specific hypothesis by instrumenting relevant code with logging, executing targeted tests, analyzing the resulting logs, and determining if the hypothesis is confirmed or refuted by the observed runtime behavior.

**Inputs:**

1.  `{TASK_GOAL}`: The original natural language description of the development task.
2.  `{TASK_NUMBER}`: The numerical identifier for the current task.
3.  `{HYPOTHESIS_NUMBER}`: The numerical identifier for the specific hypothesis being analyzed.
4.  `task_{TASK_NUMBER}.md`: The main task description file.
5.  `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: The specific hypothesis detail file to be evaluated, potentially including results from "Mental Analysis".
6.  `task_{TASK_NUMBER}_hypothesis.json`: The JSON file containing the list of all hypotheses for the task.
7.  `tests.json`: A file listing available pytest tests.
8.  Access to the project codebase and environment to run `git` and `pytest`.

**Outputs:**

1.  `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`: The **updated** hypothesis detail file with a new section appended, containing the "Code Analysis Results" (including raw logs and analysis summary).
2.  `task_{TASK_NUMBER}_hypothesis.json`: The **updated** JSON file where the status and judgement of the analyzed hypothesis are updated based on the code analysis outcome.

**Execution Steps:**

**Phase 1: Preparation and Instrumentation**

1.  **Understand Hypothesis and Context:**
    * Read `task_{TASK_NUMBER}.md` for the overall goal.
    * Thoroughly analyze `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`, focusing on the Hypothesis Statement, Key Code Locations, Key Variables, and Expected Outcome.
2.  **Identify Logging Locations & Variables:**
    * Based *strictly* on the hypothesis details, determine the precise file paths, function/method names, and line numbers for instrumentation.
    * Confirm the specific variables whose values need logging at these locations to test the hypothesis.
3.  **Commit Current State:**
    * Execute `git add .`
    * Execute `git commit -m "TEMP: Pre-instrumentation commit for analyzing task {TASK_NUMBER} hypothesis {HYPOTHESIS_NUMBER}"`. Record the commit hash for easy revert.
4.  **Instrument Code with Logging:**
    * Access the necessary code files.
    * **Constraint:** Add *only* logging statements. Do not modify existing logic.
    * In each modified file:
        * Add `import logging`.
        * Get a logger: `log = logging.getLogger(__name__)`.
        * Insert `log.debug(f"...")` or `log.info(f"...")` statements at identified locations to capture variable states, function entry/exit, arguments, return values, etc., as needed by the hypothesis. Use f-strings for clarity (e.g., `log.debug(f"Variable {var_name=} has value {var_value}")`).
        * Be sure the logging statements provide enough information to test the hypothesis. 
5.  **Identify and Execute Relevant Pytest Test(s):**
    * Analyze `tests.json` and `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` to identify the most relevant pytest test(s) to trigger the hypothesized condition.
    * Construct the pytest command: `pytest -s -v --log-cli-level=DEBUG path/to/relevant_test.py::test_function_name` (replace with actual test path).
    * Execute the command and capture the complete standard output and standard error streams.
6.  **Revert Instrumentation:**
    * **Crucially:** Revert the temporary commit made in Step 3 to remove all added logging statements and restore the original code state. Use the recorded commit hash (e.g., `git revert --no-edit <commit_hash>` or `git reset --hard <commit_hash_before_instrumentation>`). *Verify the code is clean.*

**Phase 3: Log Analysis and Synthesis**

7.  **Register Log Output (Save Raw Logs):**
    * Take the captured stdout/stderr from
    * Append this raw log output to `task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md` under a new subsection (e.g., "Raw Log Output").
8.  **Parse and Structure Logs (Conceptual):**
    * Mentally or algorithmically parse the raw logs, identifying timestamps, levels, messages, and logged variable values. Structure this information for analysis.
9.  **Filter Relevant Events:**
    * Focus on log entries originating from the instrumented locations and related to the execution flow of the chosen pytest test. Filter out unrelated noise.
10. **Sequence and Correlate Events:**
    * Order the filtered log events chronologically.
    * Reconstruct the actual execution flow based on the log sequence. Compare this to the flow expected by the hypothesis.
11. **Analyze State and Data Flow:**
    * Extract the logged values of key variables at critical points.
    * Track how these values change and flow through the execution path observed in the logs.
    * Compare the observed states/values against the "Expected Outcome" of the hypothesis.
12. **Identify Anomalies and Deviations:**
    * Look for unexpected error messages, incorrect variable values, or deviations from the expected execution path within the log sequence.
    * Did the failure event (if debugging) occur as predicted by the hypothesis?
13. **Synthesize Evaluation Outcome:**
    * Based on the log analysis (steps 9-12), determine if the evidence supports or contradicts the hypothesis.
    * Generate a clear summary explaining the findings, citing specific log entries or observed variable values as evidence.
        * **If Supported:** Explain how the logs match the expected outcome.
        * **If Contradicted:** Explain which log entries or states disprove the hypothesis.

**Phase 4: Output and Next Steps**

14. **Update Hypothesis Detail File (`task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`):**
    * Append a new section (or update the existing analysis section if iterating) to the end of the file:
        ```markdown
        ---

        **10. Code Analysis Results:**

        * **Executed Test(s):** [List the pytest command(s) run]
        * **Raw Log Output:**
            ```
            [Paste the captured raw log output here]
            ```
        * **Analysis Summary:**
            * **Outcome:** [Code Supported | Code Contradicted]
            * **Evidence:** [Insert the summary paragraph generated in Step 13 here. Explain how specific log entries/variable states confirm or refute the hypothesis.]
        * **Recommendation:** [Suggest next step based on outcome, e.g., "Proceed with coding strategy based on confirmed hypothesis.", "Hypothesis refuted, generate new hypothesis.", "Analysis inconclusive, needs different test/logging."]

        ```
15. **Update Hypothesis JSON (`task_{TASK_NUMBER}_hypothesis.json`):**
    * Read the existing JSON content.
    * Find the JSON object where `hypothesis_id` matches `Hypothesis_{HYPOTHESIS_NUMBER}`.
    * Update the `status` field for that object to reflect the outcome (e.g., `"status": "code_supported"`, `"status": "code_contradicted"`).
    * Update the `judgement` field for that object to reflect the outcome (e.g., `"judgement": "code_supported"`, `"judgement": "Explanation of contradiction"`).
    * Write the updated list back to `task_{TASK_NUMBER}_hypothesis.json`.
16. **Determine Next Action:**
    * **If `Code Supported`:** Proceed to execute the coding strategy outlined in `task_{TASK_NUMBER}.md` based on the validated hypothesis.
    * **If `Code Contradicted`:** Trigger the generate_task_hypothesis.md rule again to formulate a new hypothesis based on the latest findings.
    * **If inconclusive:** Potentially re-run analysis with different tests/logging or generate a new hypothesis.

**Completion:** The hypothesis detail file (`task_{TASK_NUMBER}_hypothesis_{HYPOTHESIS_NUMBER}.md`) is updated with the code analysis results, logs, and recommendation. The overall hypothesis list (`task_{TASK_NUMBER}_hypothesis.json`) reflects the updated status. The next action (coding or generating a new hypothesis) is determined.
