
Here is the synthesized workflow for an AI coding assistant tackling complex problems. Consider it  be in 4  rules files.

build\_contextual\_documentation.md

generate\_hypothesis.md

analyze\_hypothesis\_mentally.md

analyze\_hypothesis\_logs.md

### **1\. Build Contextual Documentation**

This initial step involves the AI gathering and structuring information to build a comprehensive understanding of the code relevant to the task. This mirrors how humans build mental models but leverages AI's capacity for large-scale analysis.

`The information to be included in task_1_context.md:`  
**Information Tracked**

 To perform comprehension or modification tasks, developers need to keep several types of information actively accessible (either in WM or readily retrievable from external aids):

* The immediate goal or objective of the current task.  
* Names and current or expected values/states of relevant variables.58  
* The purpose of key functions or methods being analyzed or called.  
* Relevant file names and their locations within the project structure.  
* **Record Focus Points:** List the top **Focus Points** file paths where we should start the analysis

**Error summary logs**

	Write the error logs and any useful information related that will help to debug it

	Do not hypothesize the reason, just facts.

**Commit evolutions**

	Analize git log \--follow  files versioning and generate a summary

**Mental Model Representation**

**Goal:** Generate representations (structure, behavior, dependencies, semantics) focused *only* on what's needed for a specific task, producing context-aware summaries at various abstraction levels.

**Strategy:** Opportunistic Comprehension \- Goal-driven, hypothesis-based exploration, mixing top-down and bottom-up analysis as needed, focusing only on relevant code sections to efficiently build a *sufficient* understanding for the task.

**Input:** A specific task goal (e.g., "Understand how user authentication is handled in the `auth.py` module to implement multi-factor authentication feature \#456", "Debug null pointer exception occurring in `process_data` function traced from error log").

**Step-by-Step Instructions:**

## 1\. Inputs and Goals

- **Task Goal:** A natural-language description of what you need to achieve (e.g., “Implement multi-factor authentication in `auth.py`”, or “Fix null pointer exception in `process_data`).  
- **Context File:** `task_1_context.md` (preloaded context; update as you discover new facts).  
- **Dependency File:** `task_1_function_dependencies.md` (to be populated with hierarchical function and module dependencies).

  ## 2\. Step-by-Step Procedure

  ### **Step 1: Parse and Identify Focus Points**

1. **Extract Keywords:** From the Task Goal, identify file names, function names, error messages, or key concepts (e.g., `auth.py`, `process_data`, `NullPointerException`).  
2. **Locate Artifacts:** Perform a semantic or text search within the codebase to find files or definitions matching those keywords.  
3. **Record Focus Points:** List the top matches (file paths, function signatures) as your initial Focus Points.

   ### **Step 2: Module-Level Dependency Analysis**

1. **Inspect Imports/Exports:** For each Focus Point’s file, list:  
   - Modules it imports.  
   - Modules that import it.  
2. **Summarize Dependencies:** Record in `task_1_function_dependencies.md`:

   \- \`auth.py\`

     \- Imports: \`database.py\`, \`utils.py\`

     \- Imported by: \`server.py\`

3. **Relevance Check:** Mark which dependencies are directly relevant to the Task Goal and enqueue them for deeper exploration.

   ### **Step 3: Local Function-Level Analysis**

1. **Open Definition:** Retrieve the code for each Focus Point (function or class).  
2. **Inspect Signature:** Note parameters, return types, and any type hints or docstrings.  
3. **Summarize Semantics:** Write a concise description (1–2 sentences) of what it does.  
4. **Identify Key Calls:** List any function calls or class usages inside.  
5. **Enqueue Callees:** If a called function seems important, add it to the exploration queue.

   ### **Step 4: Call Relationship Exploration**

1. **Find Callers:** Search for where the Focus Point is invoked in the codebase.  
2. **Summarize Context:** Note why and how it’s used in callers.  
3. **Enqueue Callers:** If a caller is relevant to the Task Goal, add it to the queue.

   ### **Step 5: Iterative Exploration Loop**

   Repeat until you have sufficient context:  
1. **Select Next Item:** Choose the highest-priority function or module from the queue (based on relevance to the Task Goal).  
2. **Relevance Decision:** If it’s no longer relevant, remove it. If it adds value, analyze it starting at Step 3\.  
3. **Update Context:** Add summaries and dependency updates to your context files.  
4. **Stop Condition:** When you can confidently answer the Task Goal or have mapped the necessary flow.

   ### **Step 6: Synthesize Context-Aware Summary**

1. **Function-Level Summary:** Detailed description of the main Focus Point(s), including key callees and callers.  
2. **Module-Level Summary:** Overview of each explored module’s purpose, imports, and exports relevant to the Task Goal.  
3. **Cross-Module Flow:** Visualize or describe the interaction path among modules/functions that fulfill the Task Goal.  
4. **Output Formats:** Provide both:  
   - A human-readable narrative.  
   - Updated `task_1_context.md` and `task_1_function_dependencies.md` with all findings.

     
     This flow emphasizes iteratively building just enough understanding, focused by the task goal, using a mix of dependency analysis, local code analysis, and exploration of call relationships, mirroring the efficiency of human opportunistic comprehension strategies.

### **2\. Generate the Hypothesis**

Once sufficient context is built, the AI formulates specific, testable hypotheses about the code's behavior, potential issues, or implementation approaches relevant to the task.

	  **Identify Potential Causes / Implementation Paths:**

* **Analyze**   
  * `task_1.md`  
  * `task_1_context.md`   
  * `task_1_function_dependencies.md`   
  * `task_1_hypothesis.json`

**Rubber Duck Analysis**

	Action: Simulate "Explaining Aloud"

Generate a detailed, structured internal articulation (or log entry) of your current reasoning state, covering the following points explicitly:

1. Re-state Goal: "Current objective: \[Clearly state the specific bug being debugged or feature being implemented\]."  
2. Summarize Key Context: "Relevant contextual information gathered so far includes: \[Briefly list key findings about involved functions/modules, important dependencies, problematic input data, error messages, etc.\]."  
3. List Prior Hypotheses (if applicable): "Previous hypotheses considered and rejected: \[List prior hypotheses and the primary reason/evidence for rejection for each\]. `task_1_hypothesis.json`"  
4. Verbalize Sticking Point: "The current reasoning impasse is: \[Describe the specific difficulty, e.g., 'cannot determine how variable X becomes null', 'unclear which component performs transformation Y', 'traces do not show expected interaction Z', 'conflicting information from sources A and B'\]."  
5. Expose Assumptions: "Current assumptions about the relevant code's behavior are: \[Explicitly list assumptions being made, e.g., 'assuming function A always returns non-null', 'assuming configuration B is active', 'assuming interaction with service C is error-free'\]."  
6. Logical Step-Through (Re-Reasoning): "Reviewing the logical sequence: \[Describe step-by-step how the current understanding leads to the sticking point, based on the context and assumptions\]."

   Expected Outcome: This structured articulation process aims to force the identification of:

* Flawed or Unverified Assumptions: Explicitly stating assumptions may reveal they lack evidence or are contradicted by context.  
* Logical Gaps or Inconsistencies: The step-by-step re-reasoning may uncover flaws in the logical chain.  
* Misinterpreted or Ignored Context: Summarizing context might highlight relevant information that was previously overlooked.  
* New Avenues for Exploration: The articulation itself can suggest new questions, angles, or hypotheses that were not previously apparent.

	**Action (for Debugging):**

* For debugging tasks, this involves hypothesizing potential root causes for observed errors, informed by error messages, stack traces, code structure around the failure point, and patterns from historical bug data  
* **Action (for Implementation):**  
  * Identify candidate functions or classes for modification based on the task requirements and existing structure (using dependency graphs, call hierarchies).  
  * Analyze existing design patterns and architectural constraints to determine appropriate integration points.  
  * Consult relevant documentation or code comments for intended usage patterns.  
  * Predict potential impacts on dependent modules based on   
  * dependency analysis.

  **Formulate Specific, Testable Hypotheses:**

* **Action:** Translate the potential causes or implementation paths identified above into explicit statements that can be evaluated. Hypotheses should be concrete and falsifiable.  
* Generate multiple hypotheses taking into account previous hypotheses and rank them based on likelihood or potential explanatory power.  
* **Decision Factors:**  
  * **Simplicity/Parsimony:** Prefer simpler explanations.  
  * **Evidence Fit:** How well does the hypothesis match the observed error/context?  
  * **Pattern Frequency:** Is this a common type of bug/solution in similar contexts (based on training data)?  
  * **Recency Bias:** Hypotheses related to recent code changes might be prioritized for regression bugs.  
  * **Estimated Evaluation Cost:** Simpler-to-test hypotheses might be prioritized.

  **Record Hypotheses:**

   Create a file `task_1_hypothesis_1.md`   
    .This file serves as a structured input for the AI agent executing the code-based hypothesis evaluation step you defined previously. Its purpose is to clearly state the hypothesis and provide all necessary information to guide the log instrumentation, test execution, and subsequent log analysis.

    **1\. Hypothesis ID:**

* A unique identifier for this specific hypothesis within the context of the task.  
* *Example:* Hypothesis\_1

  **2\. Source Task:**

* A reference back to the main task description file.  
* *Example:* Source Task: task\_1.md

  **3\. Hypothesis Statement:**

* A clear, concise, and **testable** statement describing the suspected cause of the bug or the specific code behavior being investigated. This is the core claim to be evaluated.  
* *Example:* "The AttributeError: 'NoneType' object has no attribute 'id' in process\_order occurs because the get\_customer\_details(customer\_id) function returns None when the customer\_id does not exist in the cache, and the calling code does not check for None before attempting to access customer.id."

  **4\. Rationale / Triggering Condition:**

* A brief explanation of *why* this hypothesis is being proposed. This might reference specific error messages, stack traces, code patterns observed in task\_1\_context.md, or logical deductions. It should also mention any specific conditions under which the hypothesized behavior is expected to occur.  
* *Example:* "Rationale: The error occurs intermittently. Stack trace points to line 75 in order\_processor.py. Analysis of get\_customer\_details in customer\_cache.py (from task\_1\_context.md) shows it returns None on cache miss. Hypothesis assumes a cache miss scenario triggers the bug."

  **5\. Key Code Locations for Logging:**

* Lists the specific files, functions/methods, and approximate line numbers that are critical for observing the behavior related to the hypothesis. This directly informs Step 2 (Identify Logging Locations) of the debugging instructions.  
* *Example:*  
  * customer\_cache.py: get\_customer\_details function (log entry with customer\_id, log return value).  
  * order\_processor.py: process\_order function (log entry, log the result of the get\_customer\_details call just before line 75).  
    **6\. Key Variables / State to Observe:**  
* Identifies the specific variables, parameters, or object attributes whose state needs to be captured in the logs at the locations specified above to confirm or refute the hypothesis. This informs Step 3 (Instrument Code) of the debugging instructions.  
* *Example:*  
  * In get\_customer\_details: customer\_id parameter, the value being returned.  
  * In process\_order: the value assigned to the customer variable after the get\_customer\_details call.  
    **7\. Expected Log Output (Confirmation Criteria):**  
* Describes what pattern or specific values should be observed in the logs **if the hypothesis is true**. This defines the success condition for the hypothesis and guides Step 5 (Analyze Log Output).  
* *Example:* "Expected Logs: If hypothesis is true, logs should show get\_customer\_details returning None for a specific customer\_id. Subsequently, the log just before line 75 in process\_order should show the customer variable holding the value None."

  **8\. Suggested Test Case(s):**

* (Optional but helpful) Suggests specific pytest test case(s) believed to exercise the relevant code path and potentially trigger the condition described in the rationale. This informs Step 4 (Identify and Execute Relevant Pytest Test(s)).  
* *Example:* "test\_order\_processor.py::test\_process\_order\_with\_invalid\_customer\_id"  
  	  
  Update the file `task_1_hypothesis.json` with the Hypothesis Statement

### **2.1. Analyze the Hypothesis Mentally**

This step involves a preliminary, less computationally intensive evaluation of the hypothesis, analogous to human mental simulation and focused code inspection.

* **Process:**  
  * **Focused Code Analysis:** Re-examine specific code sections identified as critical to the hypothesis.  
    * `task_1.md`  
    * `task_1_context.md`   
    * `task_1_function_dependencies.md`  
    * `task_1_hypothesis_1.md`

    

1. **Static Analysis & Code Review:**

   * **Action:** Perform static analysis on the relevant code components identified in Step 1\. This mirrors focused code reading/inspection by humans. Check for:  
     * Syntactic correctness.  
     * Type consistency (if type information is available). Does the data flow align with expected types?  
     * Code style or linting violations that might indicate logical errors (using linters conceptually).  
     * Plausibility based on variable names, comments, and surrounding code structure. Does the code *look* like it performs the function assumed by the hypothesis?  
   * **Action:** Check for known anti-patterns or potential vulnerabilities related to the hypothesis.  
   * **Goal:** Identify obvious contradictions or supporting evidence in the static code structure without running it.  
2. **Simulated Execution / Symbolic Analysis:**

   * **Action:** Perform a targeted simulation or trace of the relevant code path(s) under the specific conditions defined by the hypothesis (e.g., simulate the call calculate\_discount(user\_status='guest', ...)). This is analogous to human mental simulation but can be more rigorous.  
   * **Action (Advanced):** If feasible, use symbolic execution concepts. Assign symbolic values representing the conditions (e.g., user\_status \= 'guest') and track the constraints and potential outcomes along the execution path. Can the symbolic state lead to the predicted outcome (e.g., division by a variable that constraints show must be 0)?  
   * **Action:** During simulation/symbolic analysis, track the state of key variables and control flow. Compare the simulated state transitions and outcome against the hypothesis's prediction.  
   * **Goal:** Predict the code's behavior under the hypothesized conditions without full execution, potentially covering more cases with symbolic analysis.  
3. **Contextual Consistency Check:**

   * **Action:** Compare the hypothesis and its predicted outcome against the broader contextual documentation established earlier (e.g., dependency graphs, module summaries, version history).  
   * **Action:** Check for contradictions: Does the hypothesis assume interactions that violate known module dependencies? Does it conflict with the documented purpose of a function? Does recent version history suggest the hypothesized faulty logic was recently introduced or fixed?  
   * **Goal:** Ensure the hypothesis fits within the larger understanding of the system.  
4. **Counterfactual Reasoning (Conceptual):**

   * **Action:** Briefly consider simple counterfactuals related to the hypothesis (inspired by XAI techniques). E.g., "If user\_status were 'premium' instead of 'guest', would the hypothesized failure still occur?" Does the code path change as expected?  
   * **Action:** Does the hypothesis adequately explain *why* the alternative conditions *don't* lead to the failure (if applicable)?  
   * **Goal:** Increase confidence in the hypothesis by checking its explanatory power for related scenarios.  
5. **Synthesize Evaluation Outcome:**

   * **Action:** Consolidate findings from static analysis, simulation/symbolic analysis, contextual checks, and counterfactual reasoning.  
   * **Action:** Determine the level of confidence in the hypothesis based on the evidence gathered. Is it strongly supported, partially supported, contradicted, or still uncertain?  
   * **Action:** Generate a summary:  
     * If supported: Explain the supporting evidence (e.g., "Static analysis confirms the code path exists. Simulation with user\_status='guest' leads to discount\_rate=0 at line 55, consistent with H1."). Recommend proceeding to code-based evaluation (Step 2.2 in the previous workflow) for final confirmation if needed.  
     * If contradicted: Explain the contradicting evidence (e.g., "Static type analysis shows discount\_rate cannot be 0.", "Simulation shows an early exit before line 55 when user\_status='guest'."). Reject H1.  
     * If uncertain: Highlight the ambiguities or areas needing further investigation (e.g., "The exact value loaded for guest discount depends on external configuration not analyzed yet."). Recommend specific next steps (e.g., targeted code execution, analysis of configuration files).  
   * **Goal:** Provide a clear judgment on the hypothesis based on preliminary evaluation and guide the next action in the problem-solving process.  
     **Instruction:** Save this evaluation result, in  task\_1\_hypothesis\_1.md and update the `task_1_hypothesis.json` with a summary result.  
6. **Execute the coding strategy:**  
   	Analyze the  task\_1\_hypothesis\_1.md  and execute the `task_1.md`  
   * If after several retries it fails to get a right solution, analyze the Hypothesis with Code

### **2.2. Analyze the Hypothesis with Code**

**Goal:** Evaluate a specific hypothesis about a code bug by instrumenting the relevant code with logging statements, executing a targeted pytest test, analyzing the resulting logs, and determining if the hypothesis is confirmed or refuted.

**Your Role:** You are an AI assistant performing a debugging step. You will analyze the provided context and hypothesis, instrument code *only* with logging, run tests, analyze logs, and report findings. **Crucially, you must not change any existing code logic; only add logging statements.**

**Input Files:**

* task\_1.md: Describes the overall debugging task and potentially the bug symptoms.  
* task\_1\_hypothesis\_1.md: Contains the specific, testable hypothesis you need to evaluate.  
  **Generic Instructions:**  
* Maintain focus on the specific hypothesis in task\_1\_hypothesis\_1.md.  
* Ensure all added logging uses Python's standard logging module.  
* Be precise when identifying code locations and relevant variables.  
* Clearly state your conclusions and support them with specific log evidence.  
* If any step is ambiguous or requires information not present in the provided files, state what is missing.  
    
  **Execution Steps:**

1. **Understand Hypothesis and Context:**  
   * **Instruction:** Carefully read task\_1.md to grasp the overall debugging objective and the nature of the bug being investigated.  
   * **Instruction:** Thoroughly analyze task\_1\_hypothesis\_1.md. Identify the exact claim being made. Note the specific variables, functions, and conditions mentioned.  
2. **Identify Logging Locations:**  
   * **Instruction:** Based *specifically* on the hypothesis in task\_1\_hypothesis\_1.md and determine the exact locations (file paths, function names, line numbers) where logging is required to observe the state relevant to the hypothesis.  
   * **Instruction:** Identify the specific variables whose values need to be logged at these locations to test the hypothesis. Consider logging:  
     * The value of key variables just before or after critical operations mentioned in the hypothesis.  
     * Function arguments upon entry.  
     * Return values before returning.  
     * Relevant object attributes or dictionary keys.  
     * Simple entry/exit messages for relevant functions to trace control flow.  
3. **Commit the existing files:**  
   * Write a descriptive description so it can be reverted easily after the run  
4. **Instrument Code with Pytest Logs:**  
   * **Instruction:** Access and modify the necessary code file(s) identified in the previous step.  
   * **Constraint:** **Strictly add *only* logging statements.** Do *not* modify any existing logic, variable assignments, or control flow.  
   * **Instruction:** Import the logging module in each modified file (import logging). Obtain a logger instance (e.g., log \= logging.getLogger(\_\_name\_\_)).  
   * **Instruction:** Insert log.debug(...) or log.info(...) statements at the identified locations. Use f-strings for clear output (e.g., log.debug(f"Entering process\\\_payment. User data: {user\\\_data}"), log.debug(f"Value of {variable\\\_name=}").  
   * **Instruction:** Use DEBUG level for detailed variable states or fine-grained steps. Use INFO for higher-level progress markers if helpful.  
5. **Identify and Execute Relevant Pytest Test(s):**  
   * **Instruction:** Analyze the available tests listed in tests.json Look for tests whose names or structure relate to the task\\\_1.md.  
   * **Instruction:** Construct the precise pytest command needed to run *only* the identified test(s) and capture logs. Use flags:  
     * \\-s (to show print statements and logs directly)  
     * \\-v (for verbose output)  
     * \\--log-cli-level=DEBUG (to ensure DEBUG level logs are displayed)  
     * Specify the path to the test file and function (e.g., path/to/test\\\_auth.py::test\\\_login\\\_failure\\\_scenario).  
   * **Instruction:** Execute the pytest command and capture its *complete* standard output and standard error streams, which will include the application logs and update the ask\\\_1\\\_hypothesis\\\_1.md with the data.  
6. **Revert the commit:**  
   * **Instruction:** **Crucially**, revert all the changes made in Step 3\. Remove the logging statements you added to restore the codebase to its original state before instrumentation. This ensures the debugging artifacts do not interfere with subsequent steps or commits.  
7. **Register Log Output (Save Traces):**  
   * **Instruction:** Systematically trace the execution flow based on your log messages and save all of them in task\_1\_hypothesis\_1.md.  
8. **Parse and Structure Logs:**

   * **Action:** Ingest the raw log data. Identify the log format (e.g., timestamp, level, message, source).  
   * **Action:** Parse each log entry into a structured format (e.g., JSON objects with fields like timestamp, level, thread\_id, request\_id, source\_location, message, extracted\_variables). Leverage pattern recognition or predefined parsing rules if available. This aligns with the concept of log abstraction found in automated analysis techniques.  
   * **Goal:** Convert unstructured text into machine-readable events.  
9. **Filter Relevant Events:**

   * **Action:** Filter the structured log events based on the current hypothesis and task context. Criteria include:  
     * Time window relevant to the event/bug.  
     * Specific source code locations (files, functions) mentioned in the hypothesis or known to be involved.  
     * Relevant request IDs, session IDs, or thread IDs (crucial for distributed tracing context).  
     * Log levels (e.g., ERROR, WARN, or specific DEBUG messages related to the hypothesis).  
     * Keywords related to the hypothesis or task goal.  
   * **Goal:** Reduce noise and focus on potentially causal events.  
10. **Sequence and Correlate Events:**

    * **Action:** Order the filtered events chronologically.  
    * **Action:** Identify causal or temporal relationships between events. If dealing with distributed systems, correlate events across different services or components using shared identifiers (like trace IDs or request IDs).  
    * **Action:** Reconstruct the execution flow based on the sequence of relevant log entries. Compare this observed flow against the expected flow described by the hypothesis. This mirrors human forward/backward reasoning strategies.  
    * **Goal:** Understand the actual sequence of operations and data flow as reflected in the logs.  
11. **Analyze State and Data Flow:**

    * **Action:** Extract variable values or state information reported in the log messages at different points in the sequence.  
    * **Action:** Track how specific data points relevant to the hypothesis are modified or passed between components, as indicated by the logs.  
    * **Action:** Compare the observed state changes and data values against the predictions of the hypothesis. (e.g., "Hypothesis predicted variable x should be positive here, but the log shows x \= \-1").  
    * **Goal:** Verify if the actual runtime state matches the hypothesized state.  
12. **Identify Anomalies and Deviations:**

    * **Action:** Look for unexpected events, error messages, unusual timing patterns (e.g., excessive latency between correlated events), or deviations from normal/expected log patterns within the relevant sequence. Utilize automated anomaly detection techniques if available.  
    * **Action:** Specifically check if the failure event (e.g., the logged error message corresponding to the bug) occurs as predicted by the hypothesis's causal chain.  
    * **Goal:** Pinpoint discrepancies between observed behavior (logs) and expected behavior (hypothesis).  
13. **Synthesize Evaluation Outcome:**

    * **Action:** Based on the analysis (Steps 3-5), determine if the log trace evidence supports or contradicts the hypothesis.  
    * **Action:** Generate a clear summary of the findings, highlighting:  
      * Key log events confirming or refuting the hypothesis.  
      * Observed state values or sequences that match or deviate from expectations.  
      * Identified anomalies or errors directly related to the hypothesis.  
    * **Action:** If contradicted, provide specific evidence from the logs that disproves the hypothesis. This information should be used to refine the understanding and generate a new hypothesis.  
    * **Action:** If supported, confirm the hypothesis and document the supporting log evidence.  
    * **Goal:** Conclude the evaluation and provide actionable feedback for the next step in the reasoning process.  
      **Instruction:** Save this evaluation result, in  task\_1\_hypothesis\_1.md and update the `task_1_hypothesis.json` with a summary result.  
14. **Execute the coding strategy:**  
    	Analyze the ask\_1\_hypothesis\_1.md and execute the `task_1.md`  
    * If after several retries it fails to get a right solution, create a new hypothesis.
