# **Enhancing AI Code Generation for Complex Tasks: A Structured Prompting Workflow**

## **Section 1: Introduction**

### **1.1 The Challenge: Beyond Simple Code Generation Loops**

Artificial intelligence (AI) coding assistants, such as GitHub Copilot, have demonstrated significant potential to enhance developer productivity by automating aspects of code generation.1 These tools offer benefits like code completion, accelerated task completion, and easier syntax recall.1 However, their utility often diminishes when faced with complex coding tasks that resist resolution through simple, iterative cycles of code generation, error identification, and correction. This common "code \-\> error \-\> fix error" loop frequently fails when the underlying problem requires deeper semantic understanding or intricate logical reasoning \[User Query\].

The failure of this basic interaction model stems from fundamental limitations in current Large Language Models (LLMs) that power these assistants. While proficient at recognizing and reproducing patterns from vast training datasets 2, LLMs often lack a deep semantic comprehension of the code they manipulate.2 Their primary mechanism, often based on next-token prediction 5, may not inherently equip them with the ability to grasp complex program semantics or engage in multi-step logical inference required for non-trivial problems.2 Consequently, LLMs can generate code that is syntactically correct and appears plausible ("hallucinations") but contains subtle logical flaws, compilation errors, runtime issues, or fails to meet the specified requirements.1 Developers using these tools report spending a significant portion of their time (nearly 38% in one study) verifying suggestions, debugging, testing, and editing the generated code.1

This challenge is compounded by the inherent nature of software development itself. It is widely recognized as an intellectually demanding activity 6, often involving the resolution of problems within specific application domains (e.g., finance, physics) in addition to the programming task itself.7 Developers frequently lack critical domain knowledge required to understand complex requirements fully.7 Furthermore, human cognition faces limitations, including bounded working memory and susceptibility to biases, which can impact problem-solving performance.8 Activities like code comprehension, which can consume up to 70% of a developer's time, especially with poor documentation 11, and debugging 12, are critical yet cognitively taxing. Naive interaction with AI assistants often fails to adequately support these complex cognitive processes. The burgeoning field of LLMs in Software Engineering (LLM4SE) acknowledges these issues, facing ongoing challenges related to the quality, efficiency, reliability, and trustworthiness of AI-assisted software development.13 The gap between current LLM capabilities, particularly their reliance on pattern matching and next-token prediction 5, and the sophisticated cognitive processes essential for complex software problem-solving—such as deep comprehension, structured reasoning, and mental simulation 9—explains why simple generative loops often prove insufficient. LLM-generated code might exhibit strong syntax but weak logic 1, highlighting this discrepancy.

### **1.2 The Approach: An Expert-Mimicking Prompting Workflow**

To address these limitations, this report proposes a structured, iterative prompting workflow designed to guide AI coding assistants through the resolution of complex tasks. This workflow moves beyond simple "fix this code" instructions by explicitly mimicking the systematic problem-solving strategies employed by expert human developers. It aims to leverage the AI's strengths, such as rapid pattern recognition and code generation speed, while mitigating its weaknesses in deep reasoning and semantic understanding through carefully structured guidance and interaction.2

The proposed workflow comprises three core phases, derived from established human coding practices and AI comprehension research:

1. **Phase 1: Build Foundational Understanding**: This initial phase focuses on establishing a robust understanding of the problem context, structuring the relevant information, and guiding the AI to articulate an explicit "mental model" of the code and its intended behavior. This mirrors the critical context-building and mental model formation stages observed in human code comprehension and review.12  
2. **Phase 2: Hypothesis-Driven Investigation**: Moving from understanding to analysis, this phase guides the AI through a systematic process of generating specific hypotheses about the root cause of the problem, evaluating these hypotheses (both mentally and through code-based tests), and interpreting the results. This reflects expert human debugging strategies grounded in methodical investigation rather than trial-and-error.12  
3. **Phase 3: Strategic Task Decomposition**: When a problem proves too large or complex for direct resolution, this phase employs the principle of decomposition. The AI is guided to break the task into smaller, more manageable sub-problems, allowing the workflow to be applied recursively to these focused components. This aligns with computational thinking principles and expert strategies for managing complexity.21

This structured approach necessitates a shift in how developers interact with AI assistants for complex tasks. Instead of merely instructing the AI to produce a final output, the developer engages in a more collaborative process, guiding the AI's "thought process" through prompts designed to elicit intermediate reasoning steps, context gathering, hypothesis formulation, and structured analysis. This collaborative paradigm, viewing the AI as a cognitive partner rather than just a code generator, is central to the workflow's design.10 The goal is to provide actionable prompt engineering guidance applicable to advanced AI coding environments like cursor.ai, enabling them to tackle problems where simpler methods fail. The effectiveness of such a workflow is intrinsically linked to the AI's underlying architecture, particularly its capacity for handling structured input, maintaining context across extended interactions, and performing logical operations beyond surface-level text processing.3 Technologies like transformer architectures with attention mechanisms 3, specialized adaptations for code understanding 26, and techniques for context alignment 19 are foundational enablers for realizing the potential of this guided problem-solving approach.

### **1.3 Rationale: Grounding in Cognitive Science and AI Research**

The design of this workflow is explicitly grounded in established principles from cognitive science, software engineering research, and studies on AI capabilities and limitations:

* **Mental Models**: Cognitive science emphasizes the role of mental models—internal representations of how systems work—in human understanding and interaction.20 Accurate mental models allow users to anticipate system behavior, feel confident, and adapt quickly.20 In software engineering, developers build mental models of code to comprehend, debug, and maintain it.12 Letovsky's model, for instance, describes code comprehension as an assimilation process using knowledge and information sources to construct a mental model.17 The workflow explicitly guides the AI to build and articulate such a model (Phase 1), providing necessary information sources and structure, aiming to create a functional analogue to human understanding and facilitate explainability.20  
* **Human Problem-Solving Strategies**: Expert human developers do not rely solely on trial-and-error for complex problems. They employ systematic strategies, including hypothesis generation and testing during debugging 12, and task decomposition to manage complexity.7 Computational thinking frameworks highlight decomposition, pattern recognition, and abstraction as key problem-solving elements.21 Explicit programming strategies can make developers more organized and systematic.10 The workflow incorporates these proven human strategies (Phases 2 and 3\) into the AI interaction.  
* **LLM Capabilities and Limitations**: Current LLMs excel at pattern matching and text generation based on their training data.2 However, they often struggle with deep semantic understanding, complex logical reasoning, and maintaining accuracy in contexts requiring precise interpretation of program behavior.2 They can be misled by incomplete or irrelevant context.19 Recognizing these limitations, the workflow provides explicit guidance on context gathering, structured representation, logical investigation (hypothesis testing), and complexity management (decomposition), aiming to scaffold the AI's process and leverage its strengths while compensating for its weaknesses.19

By integrating these perspectives, the workflow aims to create a more robust and effective method for utilizing AI assistants in challenging software development scenarios, moving beyond the limitations of current generative approaches.

## **Section 2: Phase 1 \- Building Foundational Understanding: Context, Structure, and Mental Models**

### **2.1 The Goal: Establishing a Shared Understanding**

The initial phase of the proposed workflow is dedicated to building a solid foundation of understanding for the AI assistant. The primary goal is to equip the AI with the necessary background information, a clear definition of the problem, and a conceptual framework—analogous to a human's mental model—of the relevant code components and their intended behavior. This mirrors the crucial initial comprehension stage observed in human software development practices, such as code review, where reviewers first build context before inspecting code details.17

This foundational step is critical because LLMs typically lack the implicit domain knowledge 7 and the broad understanding of the system context that human developers naturally possess or acquire.17 Providing insufficient, inaccurate, or misleading context can significantly hinder an LLM's ability to reason correctly about code, potentially leading it down incorrect paths.19 Therefore, Phase 1 focuses on systematically providing and organizing the information needed for the AI to form a coherent and accurate representation of the task at hand. This deliberate focus on context and structure *before* attempting solutions directly combats the tendency of LLMs to rely on superficial pattern matching.2 By forcing a deeper engagement with the problem specifics, this phase aims to prevent the AI from prematurely converging on solutions based on potentially irrelevant patterns learned during training, grounding its subsequent reasoning in the actual problem environment.17

### **2.2 Step 1.1: Prompting for Comprehensive Context Acquisition**

**Objective**: To systematically gather all pertinent information surrounding the specific coding task or issue being addressed.

**Prompting Strategy**: The interaction should begin by instructing the AI assistant to explicitly identify and request the types of information that are crucial for understanding the problem thoroughly. This mimics the information-gathering process employed by human developers and reviewers.17 Prompts should guide the AI to seek:

* **Problem Definition**: A clear statement of the problem, the desired outcome, functional requirements, and any specific constraints.17  
* **Relevant Code**: The specific code snippets, functions, or modules that are directly involved or suspected to be problematic.  
* **Code Dependencies**: Information about how the relevant code interacts with other parts of the system, including upstream callers, downstream callees, shared data structures, and relevant libraries or APIs.19  
* **Associated Artifacts**: Links to related resources such as issue tracker entries, pull request descriptions and discussions, existing documentation, or design specifications.17  
* **Execution Environment**: Details about the runtime environment, operating system, dependencies versions, or configuration settings if they are potentially relevant to the issue.  
* **Observed Behavior**: Specific error messages, stack traces, incorrect outputs, or a description of the deviation from expected behavior.

**Rationale**: Providing a broad and comprehensive context is essential for enabling the AI to form an accurate understanding.17 LLMs, lacking human intuition about relevance, benefit from explicit pointers to diverse information sources that human experts naturally consult.17 This step aims to ensure the AI has access to the necessary inputs for building a robust internal representation.

### **2.3 Step 1.2: Prompting for Structured Information Representation**

**Objective**: To organize the potentially large and unstructured information gathered in the previous step into a more logical, digestible, and structured format that facilitates AI processing and reasoning.

**Prompting Strategy**: Once the context is gathered, the next prompt should instruct the AI to process and represent this information in a structured manner. This involves:

* **Summarization**: Generating concise summaries of the core problem, goals, and key functionalities involved.33  
* **Entity and Relationship Identification**: Identifying key code entities (e.g., classes, functions, variables, data structures) and describing their primary relationships and interactions.  
* **Flow Representation**: Describing the essential control flow and data flow within the relevant code sections. This might involve generating simplified textual descriptions, pseudo-code, or potentially leveraging techniques to visualize flow if the AI or environment supports it. Focusing on flows relevant to the problem is key.19 Simplified diagrams or representations are known to aid mental model development in humans.28  
* **Abstraction**: Applying principles of abstraction by grouping related concepts, identifying high-level components, and hiding implementation details that are not immediately relevant to the core problem.21  
* **Structured Formatting**: Encouraging the use of formats like markdown tables, bulleted lists, or structured pseudo-code rather than dense natural language paragraphs to represent the information clearly.  
* **Advanced Techniques (Optional)**: For very large contexts, consider prompting the AI to apply techniques like topic modeling to identify latent themes 33 or generate natural language outlines that partition the code.26

**Rationale**: Structuring information reduces the cognitive load associated with processing complex systems, a principle observed in human problem-solving.12 Providing information in a structured format can enhance the AI's ability to process complex relationships and perform logical operations.21 Techniques like Context-Alignment suggest that LLMs benefit when input data is structured in a way that aligns with linguistic logic and hierarchy.25 This step aims to transform raw context into organized knowledge.

### **2.4 Step 1.3: Prompting for Explicit Mental Model Articulation**

**Objective**: To guide the AI to synthesize the structured information into an explicit articulation of its "mental model"—its current understanding of how the relevant code is intended to function and how it actually operates based on the provided context.

**Prompting Strategy**: The prompts in this step should ask the AI to externalize its understanding by describing key aspects of its inferred model:

* **Purpose/Goal (Specification Layer)**: "Based on the context, what is the primary purpose or intended functionality of this code segment?".17  
* **Mechanism (Implementation Layer)**: "Describe the core logic, algorithm, or sequence of operations the code uses to achieve its purpose. What are the key data structures involved?".12  
* **Connections (Annotation Layer)**: "How do specific parts of the implementation (e.g., functions, code blocks) map to the overall goals or sub-goals?".17  
* **Assumptions and Preconditions**: "What assumptions does this code make about its inputs or the system state to function correctly? What are the necessary preconditions?"  
* **Expected Behavior**: "For the main operations or functions, describe the expected inputs, outputs, and state changes."

**Rationale**: Requiring the AI to articulate its mental model serves multiple purposes. It makes the AI's internal state of understanding explicit, allowing the human developer to verify its accuracy and completeness.30 This articulated model forms the essential baseline for generating hypotheses about discrepancies between expected and actual behavior in Phase 2\.17 Furthermore, it directly addresses the need for greater AI explainability and transparency, allowing stakeholders to understand the basis of the AI's subsequent actions.23 This step aims to construct and validate an AI understanding analogous to the mental models humans use for comprehension and debugging.12

The quality of the mental model articulated by the AI at the end of Phase 1 serves as a crucial early diagnostic checkpoint. If the AI, despite receiving structured context and explicit prompting, struggles to generate a coherent, consistent, and accurate description of the code's purpose, mechanism, and expected behavior, it signals a potential deep misunderstanding or that the task's complexity might exceed the AI's current reasoning capabilities. Identifying such issues early allows for human intervention or strategy adjustment before significant effort is wasted on subsequent phases based on a flawed foundation.20 Additionally, while comprehensive context is ideal 17, practical limitations exist regarding LLM context windows and their ability to effectively process vast amounts of information without being overwhelmed or losing focus.19 Therefore, effective prompting in Phase 1 requires a balance, potentially involving iterative refinement, summarization 33, and abstraction 21 to ensure the AI receives context that is both sufficiently complete and appropriately concise for effective processing.

## **Section 3: Phase 2 \- Hypothesis-Driven Investigation**

### **3.1 The Goal: Systematically Identifying the Root Cause**

Having established a foundational understanding and an articulated mental model in Phase 1, the workflow transitions to Phase 2: Hypothesis-Driven Investigation. The goal of this phase is to move from comprehension to targeted analysis, systematically identifying the root cause of the observed problem or error. This phase directly mirrors the debugging practices of expert human programmers, who engage in a methodical process of forming and testing hypotheses rather than resorting to random code changes or unsystematic trial-and-error.12

This approach aligns closely with the scientific method: observing the phenomenon (the error or incorrect behavior), formulating hypotheses to explain the observation, predicting outcomes based on these hypotheses, and conducting tests to verify or refute them. This structured investigation contrasts sharply with the tendency of LLMs, when given simple "fix this" prompts, to generate potential solutions without explicitly articulating the underlying reasoning or the specific fault they are attempting to address.2 Phase 2 aims to impose this logical structure onto the AI's problem-solving process. This hypothesis-driven methodology directly addresses identified weaknesses in LLMs concerning complex logical reasoning and multi-step inference.2 By breaking the debugging process down into discrete, manageable steps—generating a hypothesis, evaluating its plausibility, planning a specific test, executing the test, and interpreting the results—the workflow guides the AI through a structured reasoning process that it might struggle to perform autonomously. It leverages the AI's strengths (e.g., pattern matching for suggesting potential hypotheses) at each stage while providing the necessary scaffolding for the overall logical flow.12

### **3.2 Step 2.1: Prompting for Hypothesis Generation**

**Objective**: To generate specific, plausible, and testable hypotheses that could explain the discrepancy between the code's expected behavior (as defined by the mental model from Phase 1\) and its actual observed behavior (the error or incorrect output).

**Prompting Strategy**: Instruct the AI assistant to:

* **Compare Model and Reality**: Explicitly compare the articulated mental model (expected behavior) with the observed error or incorrect output. "Identify the specific points where the actual behavior deviates from the expected behavior described in the mental model."  
* **Propose Explanations**: Based on these discrepancies, generate a list of specific, testable hypotheses about the potential root cause(s). Hypotheses should be precise statements about the program's state or execution. Examples: "Hypothesis 1: The variable user\_count is incorrectly initialized to null instead of 0 under condition X." "Hypothesis 2: The sorting algorithm fails to handle duplicate entries correctly." "Hypothesis 3: The network request to service Y times out under heavy load, leading to incomplete data."  
* **Leverage Pattern Recognition**: Encourage the AI to draw upon its training data. "Are there common programming errors or pitfalls associated with the libraries, language features, or algorithms used in this code?" This taps into the AI's pattern-matching strengths, analogous to human intuition based on experience (System 1 thinking).12  
* **Consider Error Categories**: Prompt the AI to consider different potential types of errors, such as logical flaws, incorrect data handling, configuration issues, external dependency problems, race conditions, or resource leaks.

**Rationale**: Generating explicit hypotheses focuses the subsequent debugging effort on specific potential causes, making the process more efficient and systematic than undirected exploration.12 It shifts the interaction from simply requesting a fix to actively diagnosing the problem by asking "What could be wrong, and why?"

### **3.3 Step 2.2: Prompting for Mental Hypothesis Evaluation**

**Objective**: To assess the plausibility, explanatory power, and potential impact of each generated hypothesis *before* committing resources to writing or executing test code. This involves leveraging the AI's internal representation and reasoning capabilities for a preliminary evaluation, akin to mental simulation.

**Prompting Strategy**: For each significant hypothesis generated in the previous step, prompt the AI to perform a mental evaluation:

* **Explanatory Power**: "If Hypothesis X were true, would it fully explain the observed error message or incorrect behavior? Explain the causal link."  
* **Plausibility Check**: "Based on your understanding of the code's structure and logic (from the mental model), how likely is this hypothesis? Are there parts of the code that contradict this hypothesis?"  
* **Mental Simulation**: "Mentally trace the execution flow assuming Hypothesis X is true. What would the intermediate states and final output be? Does this match the observed failure?" (This simulates the use of a 'notional machine' by human programmers).12  
* **Prioritization**: "Based on likelihood and explanatory power, rank the generated hypotheses. Which one(s) should be investigated first?"

**Rationale**: This step mimics the cognitive shortcut of mental simulation often used by human experts.12 It allows for the rapid elimination or de-prioritization of unlikely hypotheses without the overhead of setting up complex debugging environments or executing code changes. This encourages the AI to engage in a form of reasoning (analogous to human System 2 thinking) 12 and helps prune the search space efficiently. The effectiveness of this step relies heavily on the quality and accuracy of the mental model established in Phase 1; a flawed model will lead to inaccurate mental evaluations.12

### **3.4 Step 2.3: Prompting for Code-Based Hypothesis Validation**

**Objective**: To design and specify concrete actions—such as code modifications, specific tests, or targeted tracing—that can definitively confirm or refute the most promising hypotheses identified through mental evaluation.

**Prompting Strategy**: For the top-ranked hypothesis (or hypotheses), instruct the AI to propose specific validation actions:

* **Minimal Checks**: "What is the simplest code change, assertion, or check that could directly test Hypothesis X? For example, could adding a specific log statement or conditional check verify it?"  
* **Targeted Test Cases**: "Design a specific input or set of conditions that would reliably trigger the failure *if* Hypothesis X is true. What is the expected output for this test case under the hypothesis?"  
* **Debugging/Tracing Plan**: "If a direct check is difficult, outline a plan for using a debugger or code tracing to validate Hypothesis X. What specific functions should be monitored, what variables should be inspected, and at which points in the execution?" (Further detailed in Step 2.3.1).

**Rationale**: This ensures that any code execution or debugging effort is purposeful and directly linked to validating a specific potential cause.1 It avoids unfocused debugging sessions by demanding a clear plan tied to the prioritized hypothesis, making the investigation more efficient.

### **3.5 Step 2.3.1: Prompting for Strategic Debugging & Tracing**

**Objective**: If direct code checks are deemed insufficient or impractical, this step guides the AI in generating the necessary code or instructions for targeted dynamic analysis through logging or debugging traces.

**Prompting Strategy**: Based on the validation plan from Step 2.3, instruct the AI to:

* **Identify Trace Points**: "Pinpoint the key variables, function calls, or control flow decision points that are most relevant to testing Hypothesis X."  
* **Generate Logging Code**: "Generate the necessary code snippets (e.g., print statements, logging calls) to record the values of these key variables or the execution path at critical moments."  
* **Suggest Debugger Usage**: "Recommend specific breakpoints to set in a debugger and list the variables or expressions whose values should be watched during execution to test the hypothesis."  
* **Focus the Trace**: Ensure the tracing strategy is focused on the code sections implicated by the current hypothesis, avoiding excessive or irrelevant data collection.34

**Rationale**: Code tracing can be a powerful technique but is often mentally demanding for humans due to the need to track multiple states and execution paths.34 AI can automate the mechanical aspects of generating trace code or configuring debuggers. However, it requires explicit guidance on *what* information is relevant to the current hypothesis to avoid generating overwhelming amounts of useless data. This step provides that strategic guidance.

### **3.6 Step 2.3.2: Prompting for Trace Analysis & Interpretation**

**Objective**: To analyze the output generated from the code-based checks, tests, or tracing efforts (Steps 2.3 and 2.3.1) and interpret the results to definitively confirm or refute the hypothesis under investigation.

**Prompting Strategy**: Provide the AI with the collected data (e.g., log output, debugger state, test results) and ask it to perform the analysis:

* **Interpret Evidence**: "Analyze the provided trace data/test results. Does this evidence confirm or refute Hypothesis X?"  
* **Justify Conclusion**: "Explain your reasoning step-by-step, referencing specific data points from the output that support your conclusion."  
* **Iterative Refinement**: "If the hypothesis is refuted, what does this new data suggest? Propose a revised or alternative hypothesis based on these findings."  
* **Fault Localization**: "If the hypothesis is confirmed, pinpoint the exact location (e.g., line number, function) and nature of the fault based on the evidence."

**Rationale**: This step closes the loop on the hypothesis testing cycle. It requires the AI not just to execute a test but to engage in reasoning by connecting the observed evidence back to the specific hypothesis being tested. This promotes a deeper level of analysis than simply pattern matching on log files and facilitates the iterative nature of debugging, where refuting one hypothesis often leads to the generation of new ones.

## **Section 4: Phase 3 \- Strategic Task Decomposition**

### **4.1 The Goal: Managing Complexity and Enabling Focused Solutions**

When a coding task is inherently large or complex, or when the hypothesis-driven investigation in Phase 2 fails to isolate a single root cause efficiently, expert developers often resort to a powerful strategy: decomposition.7 Phase 3 of the workflow operationalizes this strategy for AI interaction. The goal is to guide the AI assistant to break down the overarching complex problem into smaller, more logically coherent, and manageable sub-problems or sub-tasks. These smaller units can then be addressed more effectively, either independently or in sequence, potentially by recursively applying the earlier phases of the workflow.

Decomposition serves as a critical mechanism for managing cognitive load and tackling problems that exceed the capacity for direct comprehension or resolution.21 By breaking a complex system into simpler constituent parts, developers (and potentially AI) can focus their attention and reasoning on a more limited scope, making analysis and solution generation more tractable.22 This phase, therefore, provides a structured approach to complexity reduction when Phases 1 and 2 prove insufficient on their own. This acts as a vital scaffolding mechanism, particularly for AI assistants. By reducing the scope of the problem being considered at any one time, decomposition implicitly reduces the amount of context the AI needs to manage and simplifies the logical reasoning chains required for analysis and solution generation. This aligns the demands of the sub-task more closely with the known limitations of LLMs regarding complex reasoning and potentially finite context windows.2

### **4.2 Step 3.1: Prompting for Effective Problem Decomposition**

**Objective**: To analyze the overall problem and the relevant codebase (informed by Phase 1 understanding) and identify logical ways to partition the task into distinct, smaller sub-problems.

**Prompting Strategy**: Instruct the AI assistant to analyze the problem and propose a decomposition strategy:

* **Analyze Structure and Goal**: "Review the overall goal of the task and the structure of the existing code (from the mental model established in Phase 1)."  
* **Identify Sub-Components**: "Identify distinct functional units, logical steps, or stages involved in achieving the overall goal. Can the problem be broken down based on these components?".21  
* **Propose Decomposition Strategies**: Suggest potential ways to divide the problem:  
  * *Functional Decomposition*: Breaking down by modules, classes, or functions with distinct responsibilities.  
  * *Sequential Decomposition*: Breaking down by steps in a process or workflow.  
  * *Complexity-Based Decomposition*: Isolating particularly complex algorithms or logic sections.  
  * *Separation of Concerns*: Separating core logic from error handling, input validation, or specific edge cases.22  
  * *Uncertainty-Based Decomposition*: Focusing on parts of the code or requirements that are poorly understood or identified as high-risk.  
* **Consider 'Assistive Value'**: "Propose a decomposition that results in sub-problems that are relatively independent and easier to understand, test, and potentially repair. Focus on logical breakpoints rather than arbitrary code divisions. How does this decomposition enhance comprehensibility (AssistV)?".22 The concept of Assistive Value explicitly introduces a human-centric metric, guiding the AI to optimize the decomposition not just for its own processing but for clarity and maintainability, thereby fostering better human-AI collaboration.22  
* **Define Interfaces**: "For the proposed sub-problems, clearly define the inputs, outputs, and interactions (interfaces) between them."

**Rationale**: Decomposition is a fundamental technique in computational thinking and software engineering for managing complexity.7 Prompting the AI to propose a decomposition strategy encourages a structured approach to tackling large problems. However, finding an *optimal* decomposition is often non-trivial, even for humans.22 Programming involves multiple levels and types of abstraction, making decomposition inherently complex.7 Therefore, human oversight is crucial in this step to evaluate the AI's proposed decomposition and potentially guide it towards a more effective strategy based on domain knowledge and experience. The AI's proposal should be seen as a suggestion to be critically reviewed, not an absolute directive.

### **4.3 Step 3.2: Guiding Iterative Application to Sub-Problems**

**Objective**: To systematically address each sub-problem identified during decomposition by recursively applying the structured workflow (Phases 1 and 2\) to these smaller, more focused units.

**Prompting Strategy**: For each sub-problem defined in Step 3.1, guide the AI through the process:

* **Focus on Sub-Problem**: "Let's now focus exclusively on Sub-Problem X: \[Provide definition and interface constraints\]."  
* **Re-establish Context (Phase 1\)**: "Build the context, structure the information, and articulate a mental model specifically for this sub-problem. The scope is now limited to \[relevant code sections/functions\]." (The context required should be significantly smaller and more manageable).  
* **Investigate (Phase 2\)**: "Generate and test hypotheses related to achieving the goal of this sub-problem or fixing errors within it, following the hypothesis-driven investigation steps."  
* **Integrate and Iterate**: "If Sub-Problem X is successfully solved/implemented, describe how the solution integrates with the other components based on the defined interfaces. Then, let's move to the next sub-problem."  
* **Further Decomposition (If Needed)**: "If this sub-problem still proves too complex to solve directly, can it be decomposed further?"

**Rationale**: Applying the workflow recursively allows for a focused and systematic approach to problem-solving at a scale that is more likely to be within the AI's effective reasoning capabilities. It mirrors the divide-and-conquer strategy commonly used by humans to tackle large and complex projects.7 Each sub-problem benefits from the structured approach of context building and hypothesis testing, applied within a more constrained scope.

### **Summary Table: Prompting Workflow for Complex Coding Tasks**

The following table summarizes the key steps and prompting elements of the proposed workflow, providing a quick reference for practical application.

| Phase | Step | Objective | Key Prompting Elements / Questions |
| :---- | :---- | :---- | :---- |
| **1: Build Understanding** | 1.1 | Gather comprehensive context | "What is the problem/goal?" "Identify relevant code, dependencies, artifacts." "What is the error/observed behavior?" |
|  | 1.2 | Structure the gathered information | "Summarize the core problem." "Identify key entities/relationships." "Describe control/data flow." "Represent using lists, tables, or pseudo-code." |
|  | 1.3 | Articulate AI's mental model | "What is this code's purpose (Specification)?" "How does it work (Implementation)?" "How do parts map to goals (Annotation)?" "What are its assumptions?" |
| **2: Investigate** | 2.1 | Generate testable hypotheses for the error | "Compare expected (model) vs. actual behavior." "Propose specific hypotheses (Why is it failing?)." "Consider common error patterns." |
|  | 2.2 | Mentally evaluate hypothesis likelihood | "If true, does hypothesis explain the error?" "How likely is it based on the code?" "Mentally trace execution assuming hypothesis." "Prioritize hypotheses." |
|  | 2.3 | Plan code-based hypothesis validation | "What minimal check/test verifies this?" "Design a targeted input/test case." "Outline a debugging/tracing plan if needed." |
|  | 2.3.1 | Plan strategic tracing/debugging | "Identify key variables/control points for tracing." "Generate logging code." "Suggest debugger breakpoints/watches." |
|  | 2.3.2 | Analyze trace/test results | "Does this output confirm/refute the hypothesis?" "Explain reasoning based on data." "If refuted, suggest new hypothesis." "If confirmed, locate fault." |
| **3: Decompose (If Needed)** | 3.1 | Decompose complex problem into smaller sub-problems | "Identify logical sub-components/steps." "Propose decomposition (functional, sequential, etc.)." "Consider 'Assistive Value' for clarity." "Define interfaces." |
|  | 3.2 | Apply workflow recursively to sub-problems | "Focus on Sub-Problem X." "Re-run Phase 1 (context) for this sub-problem." "Re-run Phase 2 (investigation) for this sub-problem." "Integrate solution." |

## **Section 5: The Human Role \- Oversight, Critical Thinking, and Collaboration**

### **5.1 Beyond Automation: The Necessity of Human Engagement**

While the proposed workflow aims to significantly enhance the capabilities of AI coding assistants in tackling complex tasks, it is crucial to recognize that it guides the AI rather than replacing the human developer. Effective software development, especially for challenging problems, necessitates ongoing human judgment, critical thinking, and oversight.1 The workflow is designed to structure the *collaboration* between human and AI, not to achieve full automation.

Research indicates that over-reliance on generative AI tools can potentially lead to a reduction in critical engagement from users, particularly for tasks perceived as routine or lower-stakes.36 There is a concern that long-term dependence could diminish independent problem-solving skills.36 As AI tools become more integrated into development workflows, the developer's role naturally shifts. Less time may be spent on routine code generation or initial drafting, but more effort must be invested in overseeing the AI, verifying the correctness and quality of its outputs, debugging potentially subtle errors, and integrating the generated code into the larger system.1 Software development remains an intellectually challenging activity 6, and AI tools, even when guided by sophisticated workflows, are cognitive aids, not infallible oracles. The human developer remains the ultimate arbiter of quality, correctness, and alignment with requirements. This evolution transforms the developer's role towards that of a 'cognitive director' or 'debugging strategist'.1 They leverage the AI as a powerful tool for exploration, hypothesis generation, and code production, but they use the structured workflow to direct the AI's efforts, critically evaluate its outputs, and make key strategic decisions throughout the problem-solving process.

### **5.2 Prompting Strategies for Effective Human Oversight**

To facilitate this crucial human oversight role within the workflow, specific prompting strategies can be employed to encourage critical assessment and ensure transparency:

* **Verification and Explainability Prompts**: Regularly instruct the AI to justify its proposals and articulate its reasoning process. This aligns with the need for AI transparency and explainability.23  
  * "Explain the reasoning behind choosing this specific algorithm/approach."  
  * "What assumptions did you make when generating this code/hypothesis?"  
  * "What are the potential trade-offs, risks, or edge cases associated with this solution?"  
* **Critical Assessment Prompts**: Encourage active questioning of the AI's output rather than passive acceptance. Prompt the AI to consider alternatives or critique its own suggestions. This directly counters the risk of reduced critical engagement.36  
  * "Generate two alternative approaches to solving this sub-problem."  
  * "Identify potential weaknesses, limitations, or failure modes in the solution you just proposed."  
  * "Argue *against* the hypothesis you previously suggested as most likely." (Adversarial prompting)  
* **Feedback Loop Prompts**: Structure interactions to clearly incorporate human feedback and guide iterative refinement.  
  * "Based on my observation that \[specific feedback\], revise the proposed hypothesis/code."  
  * "The previous approach failed because \[reason\]. Generate a new solution that addresses this specific issue."  
* **Provenance Awareness Considerations**: Developers aware of whether code is LLM-generated may employ different validation strategies and experience different cognitive loads.1 While direct prompting for provenance might be complex, developers should maintain awareness. Prompts could ask the AI to differentiate between newly generated code and modifications to existing human or AI-generated code if feasible. "Clearly delineate the code you generated versus the pre-existing code."

### **5.3 Addressing Cognitive Biases**

Cognitive biases can affect decision-making in software engineering for both humans 8 and potentially AI systems trained on human-generated data. Biases like confirmation bias (seeking evidence that confirms pre-existing beliefs) or availability bias (over-relying on readily available examples) can lead to suboptimal solutions or flawed debugging.8

The structured nature of the proposed workflow, particularly the hypothesis-driven investigation phase (Phase 2), can serve as a partial mitigation strategy. By explicitly requiring the generation and testing of multiple hypotheses, it encourages consideration of alternatives and demands objective evidence (from traces or tests) to confirm or refute claims, potentially counteracting confirmation bias.12 However, human oversight remains essential. Developers should consciously check for potential biases in the AI's suggestions (e.g., is it repeatedly suggesting solutions similar to recent examples?) and in their own evaluation of the AI's output. The critical assessment prompts mentioned above can also help surface and challenge potentially biased assumptions.

### **5.4 Building Human-AI Shared Mental Models (SMMs)**

Effective collaboration relies on team members having aligned understandings, or Shared Mental Models (SMMs), of the task, the tools, each other's roles, and the interaction process.24 Applying this concept to Human-AI teams is crucial but challenging.24 The proposed workflow actively contributes to building SMMs for code understanding:

* **Explicit AI Model**: Phase 1 directly prompts the AI to articulate its mental model of the code, making its understanding transparent to the human developer.  
* **Transparent Reasoning**: Phase 2, through hypothesis generation and evaluation prompts, reveals the AI's diagnostic reasoning process.  
* **Guided Decomposition**: Phase 3 allows the human to guide or approve the decomposition strategy, ensuring alignment on how the problem is being broken down.

While this workflow facilitates aspects of SMM development, significant challenges remain, including the inherent difficulty in measuring the "understanding" of an AI, achieving true AI explainability (especially for complex models), designing effective human-AI interfaces, and keeping the shared model synchronized as code evolves dynamically.24 The workflow represents a practical step towards fostering better shared understanding by structuring the interaction around explicit articulation of context, reasoning, and strategy. True collaboration, however, implies mutual understanding. While this workflow primarily makes the AI understandable to the human, future advancements might explore prompting the AI to better understand and adapt to the human developer's mental model, constraints, or preferred approaches, moving towards a more genuinely bidirectional SMM.23

## **Section 6: Conclusion**

### **6.1 Summary of the Iterative Prompting Workflow**

This report has detailed a structured, three-phase prompting workflow designed to enhance the ability of AI coding assistants to tackle complex software development tasks where simple iterative code-fix loops typically fail. The workflow systematically guides the AI through processes analogous to expert human problem-solving:

1. **Phase 1: Build Foundational Understanding**: Establishes comprehensive context, organizes information structurally, and prompts the AI to articulate an explicit mental model of the code and problem.  
2. **Phase 2: Hypothesis-Driven Investigation**: Employs a systematic approach to debugging by generating specific hypotheses, evaluating them mentally and through targeted code-based tests or tracing, and interpreting the results.  
3. **Phase 3: Strategic Task Decomposition**: Manages complexity by guiding the AI to break down large problems into smaller, more manageable sub-problems, to which the workflow can be applied recursively.

This approach provides a research-backed alternative to naive prompting, aiming to leverage AI strengths while mitigating weaknesses through structured interaction and explicit guidance grounded in cognitive science and software engineering principles. It represents a form of 'cognitive scaffolding' for the LLM, providing an external structure that mirrors effective human cognitive strategies (context building, hypothesis testing, decomposition) to help the AI navigate complex problems that might otherwise exceed its inherent reasoning or planning capabilities.12

### **6.2 Advantages and Potential Benefits**

Adopting this structured workflow offers several potential advantages:

* **Improved Complex Task Handling**: Provides a more robust method for addressing coding problems that involve intricate logic, subtle bugs, or require deep contextual understanding.  
* **Systematic Debugging**: Replaces potentially haphazard trial-and-error fixing with a methodical, hypothesis-driven investigation process.  
* **Enhanced Transparency**: Makes the AI's reasoning process more explicit through articulated mental models and hypothesis testing, improving explainability.23  
* **Better Human-AI Collaboration**: Fosters a more collaborative interaction model by structuring communication and facilitating the development of Shared Mental Models (SMMs).24  
* **Mitigation of LLM Limitations**: Helps compensate for known LLM weaknesses in deep semantic understanding and complex reasoning by providing external structure and guidance.2

### **6.3 Limitations and Future Considerations**

Despite its potential, the proposed workflow has limitations and points towards areas for future research and development:

* **LLM Capability Dependence**: The effectiveness of the workflow is fundamentally constrained by the underlying capabilities of the specific LLM being used, particularly its ability to handle context, follow complex instructions, and perform logical reasoning.2  
* **Increased Initial Effort**: Requires a more significant initial investment from the developer in crafting detailed prompts and guiding the AI through the phases, compared to simpler generative prompts.  
* **Decomposition Challenges**: Determining the optimal way to decompose a problem remains a difficult task, potentially requiring significant human expertise to guide the AI effectively.22  
* **SMM Measurement**: Reliably measuring and ensuring alignment between human and AI mental models remains an open research challenge.24  
* **Integration with Formal Methods**: Future work could explore integrating this workflow with more formal program analysis techniques or verification methods to enhance rigor.5  
* **Architectural Impact**: Further research is needed to understand how different LLM architectures, pre-training data, and fine-tuning methods impact their ability to effectively engage with such structured workflows.15  
* **Evolving LLM4SE Landscape**: The field of LLMs in Software Engineering is rapidly evolving, presenting continuous new challenges and opportunities related to model capabilities, evaluation, ethics, and integration into development practices.13

The practical success of workflows like the one proposed here will likely create a positive feedback loop. As developers utilize these structured interactions, they will identify areas where current LLMs excel and where they fall short (e.g., articulating clear reasoning, reliably evaluating hypotheses, proposing insightful decompositions). This real-world usage can drive demand and provide concrete direction for future LLM research and development, pushing models beyond simple code generation benchmarks towards enhanced capabilities in collaborative reasoning, context management, and strategic problem-solving.4

### **6.4 Final Thoughts: Towards More Sophisticated AI-Assisted Development**

The structured prompting workflow presented here represents a step towards realizing the potential of AI as a more sophisticated partner in the complex cognitive endeavor of software engineering. By moving beyond simple code generation and embracing interaction models grounded in human problem-solving strategies and cognitive science, we can develop AI tools that more effectively augment developer capabilities, particularly for challenging tasks. The widespread adoption of such structured, cognitively-informed interaction methods could also have implications for how programming and software engineering are taught, potentially shifting emphasis towards strategic problem-solving, critical evaluation of AI outputs, and effective human-AI collaboration, alongside traditional coding proficiency.10 Continued research and development at the intersection of Artificial Intelligence, Human-Computer Interaction, and Software Engineering remain essential to create the next generation of tools that not only automate tasks but truly enhance human cognition and creativity in software development.9

#### **Obras citadas**

1. A Study on Developer Behaviors for Validating and Repairing LLM-Generated Code Using Eye Tracking and IDE Actions \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2405.16081v1](https://arxiv.org/html/2405.16081v1)  
2. The Code Barrier: What LLMs Actually Understand? \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2504.10557v1](https://arxiv.org/html/2504.10557v1)  
3. Attention is All you Need \- NIPS papers, fecha de acceso: abril 26, 2025, [https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf)  
4. How Accurately Do Large Language Models Understand Code? \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2504.04372v1](https://arxiv.org/html/2504.04372v1)  
5. SpecEval: Evaluating Code Comprehension in Large Language Models via Program Specifications \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2409.12866v2](https://arxiv.org/html/2409.12866v2)  
6. Exploring software developers' work practices: Task differences, participation, engagement, and speed of task resolution \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/pdf/2104.07847](https://arxiv.org/pdf/2104.07847)  
7. www.cl.cam.ac.uk, fecha de acceso: abril 26, 2025, [https://www.cl.cam.ac.uk/teaching/1415/P201/ppig-book/ch1-3.pdf](https://www.cl.cam.ac.uk/teaching/1415/P201/ppig-book/ch1-3.pdf)  
8. A Tale from the Trenches: Cognitive Biases and Software Development \- College of Engineering | Oregon State University, fecha de acceso: abril 26, 2025, [https://web.engr.oregonstate.edu/\~sarmaa/wp-content/uploads/2020/08/icse20-chattopadhyay.pdf](https://web.engr.oregonstate.edu/~sarmaa/wp-content/uploads/2020/08/icse20-chattopadhyay.pdf)  
9. (PDF) Cognition in Software Engineering: A Taxonomy and Survey of a Half-Century of Research \- ResearchGate, fecha de acceso: abril 26, 2025, [https://www.researchgate.net/publication/357876228\_Cognition\_in\_Software\_Engineering\_A\_Taxonomy\_and\_Survey\_of\_a\_Half-Century\_of\_Research](https://www.researchgate.net/publication/357876228_Cognition_in_Software_Engineering_A_Taxonomy_and_Survey_of_a_Half-Century_of_Research)  
10. arXiv:1911.00046v2 \[cs.SE\] 6 Nov 2019, fecha de acceso: abril 26, 2025, [https://arxiv.org/pdf/1911.00046](https://arxiv.org/pdf/1911.00046)  
11. Using LLMs to aid developers with code comprehension in codebases \- University of Twente Student Theses, fecha de acceso: abril 26, 2025, [https://essay.utwente.nl/103120/1/Reefman\_MA\_EEMCS.pdf](https://essay.utwente.nl/103120/1/Reefman_MA_EEMCS.pdf)  
12. Debugging: The Key to Unlocking the Mind of a ... \- Purdue e-Pubs, fecha de acceso: abril 26, 2025, [https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1085\&context=enegs](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1085&context=enegs)  
13. From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2408.02479v2](https://arxiv.org/html/2408.02479v2)  
14. (PDF) The Current Challenges of Software Engineering in the Era of Large Language Models \- ResearchGate, fecha de acceso: abril 26, 2025, [https://www.researchgate.net/publication/387264205\_The\_Current\_Challenges\_of\_Software\_Engineering\_in\_the\_Era\_of\_Large\_Language\_Models](https://www.researchgate.net/publication/387264205_The_Current_Challenges_of_Software_Engineering_in_the_Era_of_Large_Language_Models)  
15. Large Language Models for Software Engineering: A Systematic Literature Review \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2308.10620v6](https://arxiv.org/html/2308.10620v6)  
16. Large Language Models for Software Engineering: A Systematic Literature Review, fecha de acceso: abril 26, 2025, [https://web.eecs.umich.edu/\~movaghar/LLM-SE-Review-2024.pdf](https://web.eecs.umich.edu/~movaghar/LLM-SE-Review-2024.pdf)  
17. arxiv.org, fecha de acceso: abril 26, 2025, [https://arxiv.org/pdf/2503.21455](https://arxiv.org/pdf/2503.21455)  
18. Cognitive Support in Software Engineering Tools \- CiteSeerX, fecha de acceso: abril 26, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=7b1c3b4cbcc119c24f8d66b80bf4abecf92aff39](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=7b1c3b4cbcc119c24f8d66b80bf4abecf92aff39)  
19. Utilizing Precise and Complete Code Context to Guide LLM in Automatic False Positive Mitigation \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/pdf/2411.03079](https://arxiv.org/pdf/2411.03079)  
20. Understanding User Mental Models in AI-Driven Code Completion Tools: Insights from an Elicitation Study \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2502.02194v1](https://arxiv.org/html/2502.02194v1)  
21. 2.1 Computational Thinking \- Introduction to Computer Science ..., fecha de acceso: abril 26, 2025, [https://openstax.org/books/introduction-computer-science/pages/2-1-computational-thinking](https://openstax.org/books/introduction-computer-science/pages/2-1-computational-thinking)  
22. aclanthology.org, fecha de acceso: abril 26, 2025, [https://aclanthology.org/2024.acl-long.629.pdf](https://aclanthology.org/2024.acl-long.629.pdf)  
23. A mental models approach for defining explainable artificial intelligence \- PubMed Central, fecha de acceso: abril 26, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8656102/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8656102/)  
24. Full article: The role of shared mental models in human-AI teams: a ..., fecha de acceso: abril 26, 2025, [https://www.tandfonline.com/doi/full/10.1080/1463922X.2022.2061080](https://www.tandfonline.com/doi/full/10.1080/1463922X.2022.2061080)  
25. Context-Alignment: Activating and Enhancing LLM Capabilities in Time Series \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2501.03747v2](https://arxiv.org/html/2501.03747v2)  
26. Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2503.17502v1](https://arxiv.org/html/2503.17502v1)  
27. ASMA-Tune: Unlocking LLMs' Assembly Code Comprehension via Structural-Semantic Instruction Tuning \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2503.11617v1](https://arxiv.org/html/2503.11617v1)  
28. (PDF) Learning from text with diagrams: Promoting mental model development and inference generation. Journal of Educational Psychology, 98, 182-197 \- ResearchGate, fecha de acceso: abril 26, 2025, [https://www.researchgate.net/publication/220041451\_Learning\_from\_text\_with\_diagrams\_Promoting\_mental\_model\_development\_and\_inference\_generation\_Journal\_of\_Educational\_Psychology\_98\_182-197](https://www.researchgate.net/publication/220041451_Learning_from_text_with_diagrams_Promoting_mental_model_development_and_inference_generation_Journal_of_Educational_Psychology_98_182-197)  
29. Human's Intuitive Mental Models as a Source of Realistic Artificial Intelligence and Engineering \- Frontiers, fecha de acceso: abril 26, 2025, [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.873289/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.873289/full)  
30. Measures for explainable AI: Explanation goodness, user satisfaction, mental models, curiosity, trust, and human-AI performance \- Frontiers, fecha de acceso: abril 26, 2025, [https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2023.1096257/full](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2023.1096257/full)  
31. AI Transparency in the Age of LLMs: A Human-Centered Research Roadmap, fecha de acceso: abril 26, 2025, [https://hdsr.mitpress.mit.edu/pub/aelql9qy](https://hdsr.mitpress.mit.edu/pub/aelql9qy)  
32. A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges \- ResearchGate, fecha de acceso: abril 26, 2025, [https://www.researchgate.net/publication/378289524\_A\_Review\_on\_Large\_Language\_Models\_Architectures\_Applications\_Taxonomies\_Open\_Issues\_and\_Challenges](https://www.researchgate.net/publication/378289524_A_Review_on_Large_Language_Models_Architectures_Applications_Taxonomies_Open_Issues_and_Challenges)  
33. Towards Leveraging Large Language Model Summaries for Topic Modeling in Source Code \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/html/2504.17426v1](https://arxiv.org/html/2504.17426v1)  
34. hammer.purdue.edu, fecha de acceso: abril 26, 2025, [https://hammer.purdue.edu/ndownloader/files/24121835](https://hammer.purdue.edu/ndownloader/files/24121835)  
35. \[2503.08738\] Shedding Light in Task Decomposition in Program Synthesis: The Driving Force of the Synthesizer Model \- arXiv, fecha de acceso: abril 26, 2025, [https://arxiv.org/abs/2503.08738](https://arxiv.org/abs/2503.08738)  
36. The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers \- Microsoft, fecha de acceso: abril 26, 2025, [https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee\_2025\_ai\_critical\_thinking\_survey.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf)  
37. xinyi-hou/LLM4SE\_SLR: Large Language Models for Software Engineering: A Systematic Literature Review \- GitHub, fecha de acceso: abril 26, 2025, [https://github.com/xinyi-hou/LLM4SE\_SLR](https://github.com/xinyi-hou/LLM4SE_SLR)