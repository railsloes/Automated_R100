# **Human Cognitive Strategies in Coding and Debugging: A Blueprint for Artificial Intelligence**

##  

[**Human Cognitive Strategies in Coding and Debugging: A Blueprint for Artificial Intelligence	1**](#heading=)

[1\. Introduction: The Cognitive Landscape of Software Development	1](#heading=)

[1.1 The Intrinsic Complexity of Coding and Debugging	2](#heading=)

[1.2 Human Cognition as a Blueprint for AI	2](#heading=)

[2\. Foundations of Code Comprehension: Mental Models and Cognitive Processes	3](#heading=)

[2.1 Defining Mental Models in Programming	3](#heading=)

[2.2 Core Comprehension Strategies	4](#heading=)

[2.3 The Influence of Experience and Expertise	6](#heading=)

[2.4 Cognitive Load in Programming	7](#heading=)

[2.5 Role of IDE Features in Shaping Mental Models and Managing Load	8](#heading=)

[3\. Debugging Strategies: From Novice Errors to Expert Tactics	10](#heading=)

[3.1 Common Debugging Patterns and Heuristics	10](#heading=)

[3.2 Contextual Factors Influencing Strategy Selection	13](#heading=)

[3.3 Insights from Online Debugging Discussions	15](#heading=)

[3.4 The Challenge of Reproducing Bugs	16](#heading=)

[4\. Planning and Information Organization: The Developer's External Mind	18](#heading=)

[4.1 Mental Organization Techniques for Complex Codebases	18](#heading=)

[4.2 The Role and Structure of Developer Journals and Debugging Documents	19](#heading=)

[4.3 Effective Note-Taking Strategies for Code Analysis	20](#heading=)

[4.4 Tools and Practices for Information Management	22](#heading=)

[5\. Bridging Human Strategies to AI Agents	23](#heading=)

[5.1 Identifying Transferable Cognitive Steps, Heuristics, and Planning Patterns	23](#heading=)

[5.2 Simulating Human-like Debugging and Planning in AI	26](#heading=)

[5.3 Addressing Gaps: Aligning AI Capabilities with Real-World Developer Needs	27](#heading=)

[6\. Conclusion: Towards More Human-Centric AI Development Tools	28](#heading=)

[6.1 Synthesis of Human Strategies	28](#heading=)

[6.2 Recommendations for AI Agent Design	29](#heading=)

[6.3 Future Directions	30](#heading=)

[Obras citadas	30](#heading=)

##  **1\. Introduction: The Cognitive Landscape of Software Development**

### **1.1 The Intrinsic Complexity of Coding and Debugging**

Software development, encompassing activities from initial coding to ongoing maintenance and debugging, represents a profoundly complex cognitive undertaking. It extends far beyond the mechanical act of writing syntax, demanding sophisticated problem-solving abilities, abstract thinking, robust logical reasoning, meticulous attention management, and significant memory recall.1 Developers must constantly navigate intricate webs of dependencies, manage state across distributed systems, and translate abstract requirements into concrete, executable logic. The process involves understanding not only the "how" of implementation but also the "why" behind design decisions and the potential ramifications of changes.4

Furthermore, empirical evidence consistently shows that developers dedicate a substantial portion of their working hours—potentially as high as 70%—to activities centered around program comprehension, such as debugging existing code, reviewing contributions from peers, or understanding code sufficiently to add new features.7 This contrasts sharply with the time spent purely on generating novel code, underscoring that the ability to effectively understand, navigate, and modify existing software systems is paramount to developer productivity and project success. The cognitive load associated with these comprehension-heavy tasks can be substantial, influenced by factors like code quality, complexity, and familiarity.10 The sheer amount of time invested in understanding code suggests that optimizing the cognitive strategies employed during comprehension and debugging holds the greatest potential for enhancing overall software development efficiency, both for human developers and the AI systems designed to assist them.

### **1.2 Human Cognition as a Blueprint for AI**

The quest to build effective Artificial Intelligence (AI) agents capable of performing complex software development tasks necessitates a deep understanding of how expert human developers approach these challenges. Observing and analyzing human strategies—including the heuristics employed, the mental models constructed, and the planning processes undertaken—provides a crucial blueprint for designing AI systems that can operate with greater efficacy and adaptability.16 The objective transcends simple task automation; it aims to imbue AI agents with the capacity to reason, strategize, and solve problems in ways that mirror human cognitive strengths.7

Current limitations in AI for software development highlight the need for such insights. For instance, significant gaps persist between the debugging challenges faced by developers, particularly in domains like Machine Learning (ML) software with its inherent probabilistic nature, and the support offered by existing research and tools.19 Studies reveal that less than half of the identified ML debugging challenges have been explicitly addressed by researchers, with many real-world issues remaining unresolved.19 Furthermore, AI agents evaluated on real-world coding tasks exhibit specific error patterns and performance degradation when encountering unexpected execution errors, indicating difficulties in robust error handling and recovery.21 These shortcomings suggest a potential mismatch between the cognitive demands of modern software development—handling ambiguity, non-determinism, complex dependencies, and contextual nuances—and the capabilities of current AI, which may rely heavily on pattern matching rather than deeper causal reasoning or hypothesis management. This report aims to synthesize research on human coding and debugging cognition, including information organization practices, to identify specific strategies and cognitive processes potentially transferable to the design of more sophisticated and effective AI software development agents.

## **2\. Foundations of Code Comprehension: Mental Models and Cognitive Processes**

### **2.1 Defining Mental Models in Programming**

Central to a developer's ability to work with software is the concept of a mental model. This refers to an internal cognitive representation of how a system—be it a specific piece of code, a component, or the entire application—functions.2 These models encompass a developer's assumptions, beliefs, and expectations about the system's behavior, structure, and interactions.16 They are the framework upon which developers build their understanding, allowing them to reason about the code's execution, predict the outcomes of changes, explain observed behavior, and diagnose failures.18

Mental models are not static constructs. They are dynamically formed and refined through various activities, including reading source code, consulting documentation, interacting with the system, debugging, and collaborating with peers.16 Consequently, they are often incomplete, may contain inaccuracies or misconceptions based on limited information or incorrect assumptions, and evolve as the developer gains more experience or encounters new aspects of the system.16 The construction and maintenance of these mental models represent a significant cognitive investment; they are described as being "expensive" to create and maintain, requiring substantial mental effort.8

The formation of mental models can be partially explained by schema theory.2 Programmers accumulate knowledge structures, or schemata, representing stereotypical programming plans, algorithms, and data structures through experience and instruction.22 When encountering new code, comprehension involves activating relevant schemata by matching code patterns to this existing knowledge. The resulting mental model can thus be viewed as a dynamic collection of these activated schemata, integrated to represent the specific system being examined.22 The accuracy and richness of these models are crucial; mismatches between a developer's mental model and the system's actual behavior can lead to confusion, errors, and reduced productivity.16 This is particularly relevant for AI-driven coding tools, where the probabilistic nature of suggestions might conflict with a developer's deterministic expectations if their mental model of the tool is inaccurate.16

### **2.2 Core Comprehension Strategies**

Developers employ several distinct strategies to build mental models and comprehend source code. These strategies are often chosen based on the task, the developer's familiarity with the code or domain, and the nature of the code itself.

* **Top-Down Comprehension:** This strategy begins with a high-level understanding of the program's purpose or domain.14 Developers leverage existing knowledge, such as domain expertise, familiarity with architectural patterns, or understanding of programming plans (stereotypical implementations of goals), to form initial hypotheses about the code's function.14 They then progressively refine these hypotheses by examining specific code details, seeking confirmation or contradiction.14 This approach is typically used when the developer has prior familiarity with the application domain or similar systems.14  
* **Bottom-Up Comprehension:** In contrast, the bottom-up approach starts with the details of the code itself.14 Developers analyze individual statements, control flow structures, and data transformations.14 They then group related low-level elements into meaningful semantic chunks or higher-level abstractions.14 This process continues iteratively, building a progressively broader understanding of the code's functionality from the ground up. This strategy is often employed when the developer lacks sufficient domain knowledge or familiarity with the specific codebase, preventing them from forming initial high-level hypotheses.14  
* **Opportunistic / As-Needed Comprehension:** Research suggests that developers frequently utilize an opportunistic or "as-needed" strategy, pragmatically blending top-down and bottom-up approaches.1 This strategy is goal-oriented and hypothesis-driven; developers focus their attention primarily on the parts of the code they deem most relevant to their current task (e.g., fixing a specific bug, implementing a feature).1 They actively seek information pertinent to their immediate goal, switching between high-level context and low-level details as needed to form an understanding most efficiently.1 This often results in a partial, yet sufficient, mental model for the task at hand, sacrificing complete understanding for efficiency.1 Studies indicate this opportunistic approach is particularly dominant among expert programmers.1  
* **Systematic vs. As-Needed:** Some research explicitly contrasts systematic strategies, involving extensive symbolic execution and detailed tracing of data and control flow, with the more pragmatic as-needed approach.1 While both may be used, the as-needed strategy appears more prevalent, especially for modification tasks where complete understanding is not the primary goal.1

The observation that developers, particularly experts, gravitate towards opportunistic strategies 1 can be interpreted as a direct cognitive adaptation to manage the inherent challenges of software complexity. Understanding large, intricate systems 8 imposes a significant cognitive load 11, potentially overwhelming limited working memory resources.2 Systematic comprehension, whether purely top-down or bottom-up, can be exhaustive and inefficient for many common tasks. The opportunistic approach acts as a heuristic, optimizing the allocation of cognitive effort by focusing only on task-relevant information. It accepts the formation of partial mental models as a trade-off for achieving specific goals more rapidly and with less mental strain. This adaptive behavior suggests that AI agents designed for software tasks should also incorporate mechanisms for efficient relevance filtering and goal-directed exploration, rather than relying solely on exhaustive analysis.

**Table 1: Core Code Comprehension Strategies**

| Strategy | Description | Cognitive Basis | When Typically Used |
| :---- | :---- | :---- | :---- |
| **Top-Down** | Starts with high-level goals/domain knowledge, then drills down to code details to confirm hypotheses. | Schema activation, existing knowledge structures, programming plans.14 | Familiar domain or codebase.14 |
| **Bottom-Up** | Starts with code statements/details, grouping them into higher-level abstractions (chunks). | Chunking, building abstractions from concrete details.2 | Unfamiliar domain or codebase.14 |
| **Opportunistic/As-Needed** | Pragmatic, goal-oriented mix of top-down and bottom-up; focuses only on task-relevant code sections. | Hypothesis-driven problem solving, cognitive load management.1 | Common in maintenance/modification tasks, experts.1 |
| **Systematic** | Involves detailed tracing of control and data flow, extensive symbolic execution. | Detailed analysis, potentially higher cognitive load. | Less common than as-needed for modification tasks.1 |

### **2.3 The Influence of Experience and Expertise**

A developer's level of experience profoundly influences their comprehension strategies, the quality of their mental models, and their overall effectiveness.1 Experts differ from novices not just in the quantity of their knowledge, but in its organization and application.

Experts possess a richer repertoire of programming plans and schemas, allowing them to recognize stereotypical implementations and patterns more readily.22 This facilitates faster top-down comprehension and more accurate mental model construction.22 They are adept at abstracting away from surface details to understand the underlying principles and structure of a problem.31 In contrast, novices often struggle to gain a holistic view of the program, have more difficulty identifying patterns, and may focus excessively on syntactic details.13 This difference in pattern recognition and abstraction ability contributes to the higher cognitive load often observed in novices during comprehension tasks.13

Furthermore, experts tend to employ more efficient comprehension strategies. They favor pragmatic, "as-needed" approaches, strategically limiting their focus to the code sections most relevant to the task at hand, thereby managing cognitive load effectively.1 They are also more skilled at selecting the most appropriate debugging strategy for a given context.29 Experts often invest more time upfront in analyzing and qualitatively understanding a problem before attempting a solution, creating conceptual models or sketches to guide their thinking.31 They also exhibit stronger self-monitoring skills, being more aware of their understanding, potential errors, and when verification is needed.31

It is important to note that expertise is not solely defined by years of experience. It encompasses a combination of accumulated knowledge (schemas, patterns), cognitive characteristics (problem representation, abstraction ability, self-monitoring), and software-specific proficiencies (understanding design patterns, architectural principles).31

### **2.4 Cognitive Load in Programming**

Programming and related activities like code comprehension and debugging are mentally demanding tasks that impose a significant cognitive load (CL) on developers.9 Cognitive load refers to the total amount of mental effort being used in the working memory.11 Human working memory has a notoriously limited capacity, capable of holding and manipulating only a small number of information chunks simultaneously (estimates range from 4 to 7 items).2 When the demands of a task exceed this capacity, cognitive overload occurs, leading to decreased performance, increased errors, and potentially frustration or burnout.10

Several factors inherent to software development contribute to high cognitive load. Program comprehension itself requires developers to track complex control flows, understand data transformations, recall language syntax and semantics, and integrate information from various sources into a coherent mental model.12 This load is exacerbated when dealing with poorly written or unfamiliar code. Specifically, research using functional Near Infrared Spectroscopy (fNIRS), a brain imaging technique, has demonstrated that poor source code lexicon—ambiguous or inconsistent identifiers and comments—significantly increases developers' cognitive load during comprehension tasks.15 This finding underscores the critical role of clear communication through code; identifiers and comments are not merely labels but crucial cues that impact cognitive processing efficiency.15 Similarly, poor readability and structural inconsistencies also contribute to increased mental effort.15

Researchers employ various methods to measure cognitive load during programming tasks:

* **Subjective Measures:** Questionnaires like the NASA-TLX ask participants to self-report their perceived mental effort, frustration, and task difficulty.11  
* **Performance Measures:** Task completion time, accuracy, and error rates can indirectly indicate cognitive load, as performance often degrades under high load.9  
* **Behavioral Measures (Eye-Tracking):** Based on the eye-mind hypothesis (that people process what they look at), eye-tracking metrics provide insights into cognitive effort.11 Longer fixation durations, increased fixation counts, and larger pupil dilation are generally correlated with higher cognitive load, indicating more intensive processing or difficulty.11 Studies show novices exhibit significantly larger pupil sizes than experts during comprehension, suggesting greater mental effort.13  
* **Physiological Measures:** Techniques like fNIRS (measuring blood oxygenation changes in the brain) 12, electroencephalography (EEG), and electrodermal activity (EDA) 10 provide direct measures of physiological responses associated with cognitive activity.

Understanding and measuring cognitive load is crucial for designing better tools, optimizing workflows, and improving developer well-being.10

### **2.5 Role of IDE Features in Shaping Mental Models and Managing Load**

Integrated Development Environments (IDEs) are ubiquitous in modern software development and play a crucial role beyond simple text editing.10 They act as sophisticated cognitive tools, actively shaping how developers build mental models and manage cognitive load during program comprehension and debugging.28

IDEs offer a suite of features designed to support cognitive processes:

* **Syntax Highlighting & Formatting:** Reduces perceptual load by making code structure visually apparent.  
* **Code Completion & IntelliSense:** Offloads memory demands by suggesting relevant methods, variables, and syntax, reducing the need to recall exact names or parameters.28  
* **Navigation Features (e.g., "Go to Definition", "Find Usages"):** Facilitate rapid exploration of code relationships and dependencies, allowing developers to trace connections without manually searching through files.28 This supports the construction of mental models representing code structure and interactions.  
* **Integrated Debuggers:** Provide tools for step-by-step execution, breakpoint setting, and variable inspection, making the dynamic behavior of code explicit and aiding in diagnosing issues.36  
* **Static Analysis & Linters:** Offer real-time feedback on potential errors, style violations, or code quality issues, guiding developers towards better practices and reducing debugging effort.39  
* **Visualization Tools:** Some IDEs or plugins offer visualizations of code structure, dependencies, or execution traces, presenting information in alternative formats that may aid comprehension.41  
* **Integrated Collaboration (e.g., Live Share):** Features that allow real-time co-editing and awareness cues modify collaborative comprehension and debugging processes, though accessibility challenges exist.42  
* **AI Assistance (e.g., Copilot):** Integrated AI tools provide code suggestions, explanations, and fixes, fundamentally altering the workflow and cognitive demands.16

These features effectively extend the developer's cognitive capabilities, functioning as external memory aids and processing assistants.28 By providing readily accessible information (e.g., method definitions, call hierarchies) and automating certain analytical tasks (e.g., finding usages, detecting errors), IDEs reduce the burden on the developer's limited working memory.28 This offloading allows developers to focus on higher-level problem-solving and understanding.

However, traditional IDEs also have limitations. They often prioritize source code as the primary artifact, offering less integrated support for managing and linking other crucial information sources like documentation, issue tracker tickets, design rationale, or architectural diagrams.33 This fragmentation can hinder developers from building a complete mental model that encompasses the broader context of the code.33

Recognizing these limitations, researchers and tool developers have explored alternative IDE paradigms. Concepts like canvas-based IDEs (e.g., Synectic) aim to improve comprehension by allowing developers to spatially arrange related code snippets and artifacts, reducing context switching and leveraging visuo-spatial cognition.9 The goal is to place relevant information closer together, either spatially or logically, and to make relationships between different artifacts explicit.33 Empirical studies comparing such approaches with traditional IDEs suggest that providing the right information at the right time and place can significantly improve comprehension accuracy and reduce cognitive load, particularly for newcomers.9

The deep integration of IDEs into developer workflows means that these tools do not merely *support* the formation of mental models; they actively *shape* them. Drawing on concepts like distributed cognition 36, the mental model is not solely an internal representation within the developer's mind but rather an emergent property of the interaction between the developer and the IDE. The tool structures the exploration process, provides external memory cues, and automates certain analyses, thereby influencing what information needs to be actively held and processed mentally. This perspective suggests that AI agents might benefit from architectures that explicitly model this interaction, perhaps utilizing external knowledge stores accessed via tool-use mechanisms, rather than attempting to construct a single, monolithic internal representation of the entire codebase and its context.

## **3\. Debugging Strategies: From Novice Errors to Expert Tactics**

### **3.1 Common Debugging Patterns and Heuristics**

Debugging, the systematic process of identifying, locating, understanding, and correcting faults in software, is an inescapable and often time-intensive aspect of development.19 Developers employ a diverse toolkit of strategies and heuristics, ranging from systematic analysis to intuitive leaps.

* **Reproducing the Bug:** Universally cited as the critical first step.37 Successfully and consistently making the bug manifest under controlled conditions is often considered the majority of the debugging effort.44 Failure to reproduce significantly hinders diagnosis and correction.37  
* **Hypothesis Testing:** A core cognitive strategy where developers formulate potential explanations (hypotheses) for the observed failure and then devise tests (e.g., code changes, specific inputs, debugger checks) to confirm or refute them.1 This is often the initial approach, especially for complex or intermittent issues where the cause is not immediately obvious.29 Effective hypothesis generation often relies on the developer's mental model of the system and experience.29  
* **Tracing and Execution Analysis:**  
  * *Backward Reasoning (Backtracing):* Starting from the point of failure (e.g., an error message, incorrect output, crash location) and working backward through the code's logic or execution history to pinpoint the root cause.29 Stack traces are invaluable aids for this.49 This is effective when symptoms are clear.29  
  * *Forward Reasoning (Execution Tracing):* Following the program's control flow from a known good state or the beginning, observing state changes and logic execution to understand how the erroneous state is reached.29 This can help build understanding and generate facts for hypothesis testing.29  
* **Divide and Conquer (Binary Search / Simplification):** A powerful isolation technique. Developers systematically disable or remove sections of code, features, or inputs to narrow down the location of the fault.29 Commenting out code blocks, simplifying test cases, or using tools like git bisect (which performs a binary search on commit history) fall under this category.38 Particularly useful in large codebases or for visual UI defects where element removal is less likely to break core logic.29  
* **Debugger Utilization:** Employing interactive debugging tools provided by IDEs is a common practice.37 Key features include setting breakpoints to pause execution at specific lines, stepping through code execution (line by line, into/over functions), and inspecting the values of variables and memory state at runtime.37 Advanced techniques like time-travel debugging (e.g., WinDbg, rr) allow stepping backward and forward through execution history, invaluable for complex or timing-sensitive bugs.44  
* **Print Statements / Logging:** A fundamental technique, especially when interactive debuggers are impractical (e.g., in production environments, long-running processes, performance-sensitive code, or concurrency issues).37 Developers strategically insert statements (printf, console.log) or use formal logging frameworks to output variable values or trace execution points.37 While simple and effective, overuse can clutter code 38, and the act of logging itself can sometimes alter timing enough to mask or change intermittent bugs.44  
* **Code Reading and Analysis:** Sometimes, the most effective approach is simply careful reading and mental simulation of the relevant code sections to understand the logic and identify flaws.22  
* **Error Message Interpretation:** Leveraging the specific error message, error code, and accompanying stack trace provided by the system or language runtime.29 This often involves searching online resources (like Stack Overflow) for explanations or known solutions related to that specific error.30  
* **Rubber Duck Debugging:** The act of explaining the code, the problem, or the debugging process aloud to another person or even an inanimate object.18 This forces the developer to articulate their assumptions and logic step-by-step, often revealing flaws or overlooked details in their own thinking.38  
* **Starting with a Minimal Working Example:** Contrasting with modifying existing broken code, this involves building up functionality from a known-good minimal state, adding complexity incrementally until the error manifests.45 This avoids the potentially vast search space of fixing complex broken code.  
* **Trial and Error:** A less systematic approach, sometimes observed in novices, involving making changes without a clear hypothesis or strategy, often by randomly adjusting parameters or code blocks.46 Generally inefficient and unproductive.46

**Table 2: Common Debugging Techniques and Heuristics**

| Technique/Heuristic | Description | Typical Scenario/Trigger | Pros | Cons |
| :---- | :---- | :---- | :---- | :---- |
| **Reproduce the Bug** | Consistently trigger the error in a controlled way. | All debugging tasks (first step). | Essential for verification, enables systematic analysis. | Can be very difficult/time-consuming for intermittent/env-specific bugs. |
| **Hypothesis Testing** | Formulate and test potential causes for the error. | Complex, intermittent, or non-obvious bugs.29 | Systematic, focuses investigation. | Requires good initial understanding/mental model; can be slow if hypotheses are poor. |
| **Backward Reasoning** | Trace execution/logic backward from the failure point/symptom. | Clear error message/symptom.29 | Direct path from effect to cause. | Can be difficult if symptoms are misleading or far from root cause. |
| **Forward Reasoning** | Trace execution forward from a known state to understand how the error state is reached. | Understanding complex logic flow, generating facts.29 | Builds understanding of program dynamics. | Can be slow, may trace irrelevant paths. |
| **Divide and Conquer** | Systematically isolate the fault by disabling/removing code sections. | Large codebases, complex interactions, UI bugs.29 | Efficiently narrows down the problem space. | May be hard to apply if sections are highly interdependent. |
| **Debugger Utilization** | Use IDE debugger to step through code, inspect state. | Most development environments, understanding runtime behavior. | Precise control over execution, direct state inspection.37 | Can be slow, may alter timing, less useful in production/some contexts. |
| **Print Statements/Logging** | Insert output statements to track execution and state. | Production, timing-sensitive issues, concurrency.37 | Simple, works in many environments. | Can clutter code, may alter timing, requires recompilation/redeployment. |
| **Error Message Interpretation** | Analyze error messages and stack traces, often searching online. | Explicit errors thrown by system/runtime.29 | Leverages specific failure information, accesses collective knowledge. | Error messages can be cryptic or misleading. |
| **Rubber Duck Debugging** | Explain the problem/code aloud. | Feeling stuck, clarifying own thoughts.38 | Forces structured thinking, often reveals assumptions/flaws. | Requires articulating the problem clearly. |
| **Minimal Working Example** | Start with working code and add complexity until failure. | Complex broken systems where fixing is difficult.45 | Avoids large search space of fixing, systematic build-up. | Requires effort to create minimal example, may not always be feasible. |
| **Code Reading/Analysis** | Carefully read and mentally simulate code logic. | Initial investigation, understanding specific functions.22 | No tools needed, deep understanding. | Can be mentally taxing, prone to misinterpretation. |
| **Trial and Error** | Make changes without a clear strategy. | Often used by novices when stuck.46 | Might stumble upon a fix eventually. | Highly inefficient, doesn't build understanding, risky. |

### **3.2 Contextual Factors Influencing Strategy Selection**

The choice of debugging strategy is rarely arbitrary. Experienced developers, in particular, dynamically adapt their approach based on a confluence of contextual factors related to both the defect itself and the codebase it resides in.29 The goal is to select the strategy most likely to be effective and efficient given the specific circumstances.

**Defect Characteristics** 29**:**

* **Clarity and Nature of the Symptom:** A clear, informative error message with a precise stack trace often prompts backward-reasoning or error-message debugging. Conversely, if the link between the observed symptom (e.g., incorrect output) and the potential root cause is obscure or involves complex logic, developers might lean towards binary search or simplification techniques. An initial step might even involve consulting documentation or stakeholders to confirm if the observed behavior is indeed a defect or an intended, albeit perhaps unexpected, feature.  
* **Reproducibility:** Consistently reproducible bugs lend themselves to systematic strategies like interactive debugging or tracing. Sporadic, intermittent defects are notoriously difficult and often necessitate hypothesis-testing, extensive logging, and careful comparison between successful and failed executions to identify subtle triggers. Binary search is generally unsuitable for sporadic bugs unless a specific trigger sequence is found, and backward-reasoning can be confounded by timing dependencies. User-specific defects require strategies focused on replicating the user's environment or analyzing user-specific data/logs.  
* **Environment (Development vs. Production):** The environment heavily constrains available strategies. Development environments typically allow full use of interactive debuggers, code modification, and detailed tracing. Production environments often restrict direct access and modification, forcing reliance on logs, monitoring data, crash dumps, and more indirect methods.  
* **Location (Client-side vs. Server-side):** The location of the defect influences strategy. Visual defects in client-side UIs often respond well to simplification (removing UI elements is less likely to break core functionality). Server-side defects, where removing code can have cascading consequences, might be approached with backward-reasoning, hypothesis testing, or adding log statements, depending on familiarity.

**Codebase Characteristics** 29**:**

* **Familiarity:** Developers deeply familiar with a codebase can leverage their mental model to form strong hypotheses and efficiently use targeted strategies like hypothesis-testing, binary search, or simplification. Understanding component interactions is key. When faced with unfamiliar code, developers often start with more exploratory strategies like forward-reasoning to grasp the architecture, libraries, and syntax. Error-message debugging or backward-reasoning might also be initial approaches. Some developers even utilize AI tools like ChatGPT to gain an initial understanding of unfamiliar code sections. A recurring challenge noted in studies is debugging code written by others.29  
* **Access (Source Code, Resources, Level):** Direct access to source code is crucial for many strategies, particularly backward-reasoning or detailed stepping in a debugger. This may not be possible in production environments with compiled code. Access to different environments (development, staging, production), specific hardware, or external services (APIs) also dictates feasible approaches. Limited access to API source code or documentation hinders debugging interactions. Replicating the production environment locally, if possible, enables a wider range of techniques. The level of access (e.g., user vs. admin privileges) further shapes the investigation.  
* **Maintenance Status and Size:** When dealing with deprecated code, developers might prioritize minimal interventions, using hypothesis-testing or backward-reasoning to understand and fix the issue without major rewrites, although sometimes replacement is necessary. Codebase size and complexity also matter; smaller, well-structured codebases facilitate forward-reasoning, while large, complex ones often push developers towards error-message debugging, hypothesis-testing, or simplification techniques. Refactoring might be employed to improve readability as part of the debugging process.

This dynamic interplay highlights that debugging is not a monolithic skill but a context-sensitive application of various techniques. The debugging process itself is iterative and knowledge-driven. Initial actions, like attempting reproduction or examining an error message, provide crucial information. This information refines the developer's mental model of the problem, which, combined with the contextual factors, guides the selection of the next strategy. This cycle of information gathering, hypothesis refinement, testing, and strategy adaptation continues until the root cause is identified and resolved. This iterative, adaptive nature suggests that effective AI debugging agents will require mechanisms for dynamic strategy selection based on evolving internal state representations and incoming information, moving beyond fixed or purely sequential approaches.

### **3.3 Insights from Online Debugging Discussions**

Online platforms, particularly Stack Overflow, serve as vast repositories of collective debugging knowledge and reveal common practices and challenges.30 Developers routinely turn to these forums when encountering errors or seeking solutions.30

Analysis of search behavior shows differences based on experience: experts tend to formulate more precise search queries, often including specific code snippets or error messages, and are more likely to investigate results beyond the top-ranked links compared to novices.30 Novices may struggle with formulating effective queries and applying the found solutions due to insufficient background knowledge.30

Discussions on platforms like Stack Overflow and Hacker News echo many established debugging principles:

* The paramount importance of **reproducing the bug** is frequently emphasized.44  
* **Starting with minimal working examples** is advised over trying to fix complex broken code directly.45  
* **Hypothesis testing** and thinking systematically are common themes.47  
* Techniques like **divide and conquer** (git bisect), **checking basic assumptions** ("check the plug"), and **rubber ducking** are shared strategies.45  
* The utility and limitations of **debuggers versus print statements/logging** are often debated, with context dictating the best approach.44  
* The value of **keeping logs** of debugging attempts is mentioned.45

Stack Overflow, in particular, often focuses on specific error types, like the StackOverflowException caused by excessive recursion or stack exhaustion.49 Solutions typically involve analyzing the stack trace provided in the error message or using a debugger to examine the call stack at the point of failure to identify the repeating or deeply nested calls.49

The heavy reliance on these online resources indicates that a significant component of practical debugging involves leveraging shared community knowledge. Developers frequently engage in pattern matching, searching for solutions to problems similar to their own that others have already encountered and documented. This external knowledge base effectively supplements their individual experience and mental models. Consequently, debugging in practice is often not a purely deductive process from first principles but incorporates recognizing and adapting known solutions from the wider community. This strongly suggests that AI agents could achieve significant performance gains by being equipped with mechanisms to effectively query and integrate information from these vast online knowledge repositories.

### **3.4 The Challenge of Reproducing Bugs**

While reproducing the bug is the cornerstone of effective debugging 37, it is frequently one of the most challenging steps, particularly for certain classes of errors.44

Key challenges include 44:

* **Intermittency:** Bugs that occur sporadically, seemingly at random, are notoriously difficult to trigger on demand. Race conditions, timing sensitivities, or rare combinations of inputs can lead to such behavior.  
* **Environment Dependency:** Issues may only manifest in specific environments (e.g., a customer's unique hardware/software configuration, production network conditions) and resist replication in development or testing labs due to subtle differences. External factors, like voltage fluctuations, can even play a role.  
* **Hardware/Software Interaction:** Problems originating in hardware can present as software bugs, making software-only reproduction attempts futile.  
* **Concurrency and Timing:** Bugs arising from the interaction of multiple threads, processes, or hardware components are highly sensitive to timing and system load. Attempts to observe the bug (e.g., adding logging) can alter the timing enough to make the bug disappear or change its behavior.  
* **Elusive Triggers:** The bug might require a very specific, complex, or rare sequence of user actions, data inputs, or system states to occur.  
* **Organizational Barriers:** Lack of access to the affected system, source code, relevant logs, or knowledgeable personnel can prevent effective investigation and reproduction.

Strategies employed to overcome these challenges often require persistence, creativity, and systematic investigation 44:

* **Persistence and Creative Speculation:** Relentlessly pursuing the issue, forming creative hypotheses about potential triggers, and sometimes building specialized hardware or software mocks to simulate suspected conditions.  
* **Enhanced Logging and Tracing:** Implementing detailed, robust logging or tracing mechanisms to capture system state and execution flow, hoping to catch relevant information when the bug does occur, even if infrequently.  
* **Time-Travel Debugging:** Using advanced debuggers (e.g., WinDbg, rr) that record execution history, allowing developers to examine the program's state leading up to the failure after it has occurred.  
* **Automated Reproduction:** Employing scripts or even physical robots to repeatedly perform actions or generate inputs that are suspected triggers, especially for hardware interaction issues.  
* **Systematic Elimination/Isolation:** Methodically ruling out potential contributing factors or isolating system components to narrow down the conditions required for the bug to manifest.  
* **Challenging Assumptions:** Actively questioning initial beliefs about the bug's cause and exploring alternative explanations.  
* **Artificial Error Injection:** Deliberately introducing controlled errors (e.g., network packet loss, disk errors) to see if they trigger the observed failure mode, helping to confirm hypotheses about system sensitivities.

Successfully reproducing a difficult bug often requires moving beyond standard debugging techniques and employing a more investigative, experimental mindset.

## **4\. Planning and Information Organization: The Developer's External Mind**

### **4.1 Mental Organization Techniques for Complex Codebases**

Navigating and understanding large, complex, and sometimes monolithic codebases presents significant cognitive challenges.8 Developers rely on various techniques to build functional mental models and manage this complexity, often integrating information from multiple sources beyond the code itself.

Effective strategies include 26:

* **Reading Documentation and READMEs:** These artifacts provide high-level context, setup instructions, architectural overviews, and explanations of intent, forming an essential starting point.26 Even outdated documentation can offer historical context.26  
* **Analyzing Commit History:** Examining commit messages and associated pull requests for specific files or modules reveals the evolution of the code, the rationale behind changes, and the developers involved.26 This historical context aids understanding.26  
* **Pair Programming:** Collaborating with developers experienced in the codebase provides invaluable high-level insights into design patterns, testing strategies, historical decisions, and implicit knowledge that may not be documented.26  
* **Reading Tests:** Unit, integration, and functional tests serve as executable specifications, demonstrating intended functionality, usage examples, and handling of edge cases or known defects.26  
* **Incremental Exploration ("Start Small"):** Beginning with a small, understandable piece of code and progressively tracing dependencies and related logic helps manage complexity by building understanding incrementally.26 This involves following import statements, analyzing function calls, or understanding generation scripts.26  
* **Studying Workflows:** Tracing the execution flow for key features or operations helps understand how different components interact and data moves through the system.27  
* **Using the Product:** Interacting with the application as an end-user provides context on its purpose and behavior, grounding code-level understanding in real-world functionality.27  
* **Focusing on Abstractions:** Mentally modeling the system in terms of major components and their interactions ("grey boxes") rather than attempting to grasp all implementation details simultaneously helps manage complexity.51 Developers dive into the specifics of a component only when necessary for a task.51

Building a robust understanding requires synthesizing information from diverse sources: the static structure of the code, its dynamic behavior (via tests or execution), its historical evolution (commits), its documented intent (docs), and human expertise (pairing). This multi-faceted information need implies that effective comprehension support, whether human or AI, must extend beyond simple code analysis to integrate and reason about these varied artifacts and knowledge types.

### **4.2 The Role and Structure of Developer Journals and Debugging Documents**

To manage the cognitive demands of coding and debugging, developers often employ external aids to organize thoughts, track progress, and structure their problem-solving process. Developer journals and debugging documents serve as crucial external cognitive tools.

* **Developer Journals:** These are typically personal, informal logs used to support the entire development workflow.52 Their uses include:  
  * **Problem Definition & Goal Setting:** Clearly articulating the problem to be solved or the goal for a coding session.52  
  * **Task Decomposition:** Breaking down larger tasks into smaller, manageable steps or to-do lists.52  
  * **Planning & Hypothesis:** Outlining intended approaches, exploring uncertainties, and formulating initial hypotheses before coding.52  
  * **Tracking Attempts & Findings:** Recording actions taken during coding or debugging, their outcomes, and any insights gained. This prevents repeating failed steps and documents solutions.52  
  * **Managing Distractions:** Jotting down unrelated ideas, questions, or potential refactorings to address later, maintaining focus on the current task.52  
  * **Information Capture:** Storing notes from meetings, links, code snippets, or future ideas.52  
  * **Reflection:** Reviewing progress, challenges, and learnings after a session or task completion.52 Journals are often kept in simple text or markdown files, sometimes within the IDE itself for quick access.52 The emphasis is on rapid capture and personal utility, not polished writing.52 Customization to individual needs and workflows is key.52  
* **Debugging Documents:** These tend to be more structured documents specifically created to manage and document the process of diagnosing a particular bug, often with collaboration in mind.48 They impose a systematic approach and typically include:  
  * **Problem Context:** Description of the issue, intended feature behavior, error logs/messages, environment where it occurred, specific steps to reproduce, and consistency of the error.48  
  * **Initial Investigation:** Identification of affected code files/functions, relevant dependencies, and analysis of recent changes.48  
  * **Hypothesis Testing:** Explicit documentation of each hypothesis, including the suspected cause, the exact steps taken to test it, observations, and the outcome (confirmed/rejected).48  
  * **Solution Documentation:** A clear explanation of the fix, analysis of the root cause, and any partial resolutions or remaining issues.48 Debugging documents facilitate collaboration by allowing others to understand the problem and the investigation steps taken. They also serve as valuable learning resources for the team, documenting solutions and diagnostic processes.48 Templates are sometimes used to ensure consistency.48

Both journals and debugging documents function as extensions of the developer's working memory and reasoning process. They are not passive records but active tools for structuring thought, managing complexity, offloading memory demands, and facilitating systematic problem-solving. This practice of externalizing the cognitive process provides strong evidence for the need for analogous mechanisms in AI agents, such as explicit logging of reasoning steps, hypothesis tracking, and plan management, to handle complex tasks effectively and transparently.

### **4.3 Effective Note-Taking Strategies for Code Analysis**

Beyond dedicated journals or debugging docs, general note-taking during code analysis, learning, or planning is a valuable habit that aids concentration and retention.53 Several structured methods can be particularly beneficial for computer science and software development contexts:

* **Cornell Method:** Divides the page into cues (keywords/questions), main notes, and a summary section.53 Useful for summarizing topics, identifying key terms, and self-quizzing, applicable to understanding concepts like data structures or operating system principles.53  
* **Outline Method:** Employs a hierarchical structure with indentation to represent topics, sub-topics, and details.53 Well-suited for organizing information about complex theoretical concepts or features with many facets, mirroring code structure itself.53  
* **Mind Mapping:** A visual technique starting with a central idea and branching out to related concepts.53 Excellent for brainstorming, visualizing relationships between components, understanding algorithms, or mapping out code logic flow.53  
* **Charting Method:** Uses columns to organize information by category, facilitating comparison and analysis of different aspects (e.g., comparing algorithms, tool features).54  
* **T-Notes Method:** Divides the page into sections for general info/title, theoretical information/formulas (left), and personal notes/questions (right).54 Suited for technical subjects involving formulas or specific code constructs.

Regardless of the method, effective notes for developers should often include 53:

* **Code Snippets:** Short, relevant examples illustrating syntax, function usage, or specific logic patterns.  
* **Annotations:** Brief comments or explanations accompanying code snippets or complex concepts.  
* **Keywords/Highlights:** Using colors or emphasis to mark important terms, concepts, or variables.53  
* **Organization:** Systematically organizing notes by project, module, subject, or date using separate notebooks, folders, or digital tags for easy retrieval.53

The choice between handwritten and digital notes involves trade-offs: handwriting may aid memory retention but lacks searchability, while digital tools offer powerful organization, search, and editing capabilities but may require setup and cause screen fatigue.53 A hybrid approach, taking quick handwritten notes during lectures or meetings and later organizing them digitally, is also viable.53

**Table 3: Overview of Note-Taking Methods for Developers**

| Method | Description | Use Case in Development | Key Benefit |
| :---- | :---- | :---- | :---- |
| **Cornell** | Page divided into Cue, Notes, Summary sections.53 | Summarizing concepts (e.g., algorithms, OS principles), review, identifying keywords. | Structured review, active recall prompts (questions/cues). |
| **Outline** | Hierarchical structure using indentation for topics/subtopics.53 | Documenting complex features, system architecture, theoretical concepts. | Clear structure, shows relationships between levels of detail. |
| **Mind Mapping** | Visual diagram linking central idea to branches of related concepts.53 | Brainstorming solutions, visualizing algorithms/data flow, understanding system components. | Visual overview, highlights connections, aids creativity. |
| **Charting** | Organizes information in columns by category.54 | Comparing different libraries/frameworks/algorithms, tracking feature attributes. | Easy comparison, structured data presentation. |
| **T-Notes** | Page divided into Top (Title), Left (Theory/Code), Right (Notes/Questions).54 | Analyzing specific code blocks, understanding technical formulas/specifications. | Separates objective information from subjective interpretation/questions. |

### **4.4 Tools and Practices for Information Management**

Developers utilize a range of tools and practices to manage the flow of information inherent in their work, supporting planning, comprehension, and collaboration.

* **Note-Taking & Organization Tools:** Beyond basic text editors 52, specialized digital tools offer enhanced features. Notion provides high customizability and database-like organization.55 Trello uses visual Kanban boards for task and workflow tracking.55 Apple Notes and Google Keep offer simplicity and ecosystem integration.55 The choice often depends on individual preference for visual vs. text-based organization, required features, and integration needs.55  
* **Planning & Design Techniques:** Effective planning precedes coding.56 This involves:  
  * *Defining Objectives:* Establishing clear goals for the project or feature.58  
  * *Task Decomposition:* Breaking large problems into smaller, manageable units.4  
  * *Pseudocode:* Sketching out logic in a semi-formal, language-agnostic way before implementation.4  
  * *Diagramming/Sketching:* Using visual aids like flowcharts, UML diagrams (Use Case, Class, Sequence, State, Deployment), or informal sketches to represent structure, flow, or interactions.4 These act as visual aids for refining mental models.25  
  * *"Code Sketching":* An iterative process of writing small, exploratory code snippets to test ideas and interact with the machine, refining concepts through rapid feedback cycles.60 This can also involve translating visual sketches into initial code outlines, potentially aided by LLMs.25 This practice mirrors design thinking, allowing for low-fidelity prototyping of logic and structure before full implementation, enabling rapid exploration and refinement of mental models.  
* **Documentation Practices:** Creating and maintaining clear documentation is vital for communication and future comprehension.26 This includes:  
  * *README Files:* Providing setup, usage, and overview information.26  
  * *Code Comments:* Explaining the *why* behind non-obvious code, not just restating the *what*.39 Meaningful comments are crucial, but excessive or redundant comments should be avoided.39  
  * *API Documentation:* Using tools like Javadoc (Java), Doxygen (C++), or Docstrings (Python) to generate formal documentation for interfaces and libraries.39  
* **Version Control Systems (VCS):** Tools like Git are indispensable for modern development.37 They enable:  
  * *Tracking Changes:* Maintaining a history of modifications.  
  * *Collaboration:* Managing contributions from multiple developers via branching and merging.39 Pull requests facilitate code review.64  
  * *Experimentation:* Allowing developers to safely explore changes on separate branches without disrupting the main codebase.58  
  * *Debugging:* Tools like git bisect help pinpoint when bugs were introduced.45  
  * *Best Practices:* Using consistent branching strategies and writing descriptive commit messages that explain the purpose and scope of changes are key.26

These tools and practices collectively form an external scaffolding that supports developers in managing complexity, organizing information, planning their work, and collaborating effectively.

## **5\. Bridging Human Strategies to AI Agents**

Understanding the cognitive strategies, heuristics, and information management techniques employed by human developers provides a rich foundation for designing more capable and human-aligned AI software development agents. The goal is to move beyond simple code generation or pattern matching towards AI systems that can reason, plan, debug, and learn in more sophisticated ways.

### **5.1 Identifying Transferable Cognitive Steps, Heuristics, and Planning Patterns**

Several core aspects of human developer cognition appear particularly relevant and potentially transferable to AI agent design:

* **Opportunistic/Goal-Directed Comprehension:** Humans rarely attempt to understand an entire large codebase exhaustively. Instead, they adopt "as-needed" strategies, focusing analysis on sections relevant to the current task or bug.1 AI agents could benefit significantly from similar goal-directed focusing mechanisms, prioritizing analysis based on task requirements rather than attempting computationally expensive exhaustive exploration. This requires robust relevance filtering and task decomposition capabilities.  
* **Hypothesis-Driven Debugging:** The human process of generating, testing, and refining hypotheses about bug causes is a powerful heuristic.1 AI agents could explicitly model this process, perhaps using probabilistic reasoning informed by error messages, code structure analysis, historical bug data, or even simulated execution traces to generate and prioritize potential fault locations and causes.  
* **Contextual Strategy Selection:** Expert developers dynamically choose comprehension and debugging strategies based on contextual factors like codebase familiarity, defect characteristics, and available tools.29 An AI agent could incorporate a similar meta-level control mechanism, learning to select the most promising analysis or debugging technique (e.g., backward tracing vs. binary search vs. querying documentation) based on the current problem state and context.  
* **Externalized Reasoning and Planning:** Developers rely heavily on external aids like notes, journals, and debugging documents to track their thought processes, manage intermediate findings, and structure complex tasks.48 AI agents could implement analogous "external reasoning" structures – explicit logs, structured scratchpads, or plan representations – to track their own reasoning steps, hypotheses tested, intermediate results, and planned actions. This would enhance transparency, facilitate backtracking, support more complex multi-step tasks, and potentially improve robustness.  
* **Leveraging Diverse Knowledge Sources:** Human comprehension integrates information from code, documentation, commit history, tests, and peer knowledge.26 AI agents should similarly be designed to ingest, process, and synthesize information from these varied sources, moving beyond purely code-based analysis. This includes natural language processing for documentation and commit messages, test execution and analysis, and potentially interfaces for querying online knowledge bases or even human collaborators.  
* **Incremental Development and Refactoring:** Complex tasks are often tackled incrementally, breaking them down and applying refactoring techniques to improve structure and maintainability along the way.58 AI agents could adopt similar incremental generation and refinement strategies, potentially incorporating automated refactoring capabilities based on code quality metrics or learned patterns.  
* **Simulated Cognitive Load Awareness:** While AI doesn't experience cognitive load, it could potentially model or estimate the "difficulty" or "computational cost" associated with different analysis paths or code sections. This could be based on complexity metrics, prediction models trained on human cognitive data (e.g., eye-tracking, fNIRS studies 10), or analysis of structural properties. Such estimations could guide the agent's strategy towards more tractable or promising avenues of investigation, mimicking human heuristic choices driven by cognitive ease.

The most impactful transfer may lie not in simply replicating individual human actions (e.g., "use print statement"), but in modeling the underlying cognitive control loops that govern expert behavior. This involves cycles of goal setting, context assessment, strategy selection (considering estimated cost/benefit), information gathering (from code, docs, execution), internal state/hypothesis updating, and action execution. Effective AI agents likely need to implement these higher-level strategic control mechanisms to navigate the complexity of real-world software development tasks.

**Table 4: Human Strategies Potentially Transferable to AI Agents**

| Human Strategy/Cognitive Process | Rationale for Transferability | Potential AI Implementation Approach |
| :---- | :---- | :---- |
| Opportunistic Comprehension | Manages complexity & cognitive load in large systems; task-focused efficiency.1 | Goal-directed analysis; relevance filtering based on task description/bug report; prioritized code exploration based on call graphs or dependency analysis. |
| Hypothesis-Driven Debugging | Systematic approach to isolate unknown faults; core human problem-solving heuristic.29 | Explicit hypothesis generation (e.g., fault localization candidates); probabilistic ranking of hypotheses; automated test generation or execution simulation to test hypotheses. |
| Contextual Strategy Selection | Adapts approach to problem specifics for efficiency; hallmark of expertise.29 | Meta-controller or policy network that selects analysis/debugging tools/methods based on input features (error type, code metrics, familiarity score, environment). |
| Externalized Reasoning/Planning | Offloads working memory, structures complex tasks, aids backtracking.48 | Maintain structured log/trace of reasoning steps, hypotheses considered, actions taken, results observed; explicit plan representation (e.g., task graph). |
| Leveraging External Knowledge | Augments internal model with docs, history, community knowledge.26 | NLP for processing documentation/commits; integration with issue trackers; ability to query/summarize web search results (e.g., Stack Overflow); test result analysis. |
| Incremental Refinement | Breaks down complexity, improves maintainability iteratively.58 | Generate initial solution drafts; apply automated refactoring rules based on quality metrics; iterative improvement cycles based on testing or analysis feedback. |
| (Simulated) Cognitive Load | Guides humans towards simpler/more tractable paths; avoids overload.11 | Estimate computational cost/complexity of analysis paths; use heuristics based on code metrics (cyclomatic complexity, coupling); prioritize simpler explanations/fixes. |

### **5.2 Simulating Human-like Debugging and Planning in AI**

Current Large Language Models (LLMs) offer significant potential for simulating aspects of human developer cognition beyond simple code generation. Tools like GitHub Copilot are already being used for tasks central to comprehension and debugging 43:

* **Explaining Code:** Generating natural language descriptions of code snippets or functions helps developers build mental models faster.43  
* **Explaining Bugs:** Providing insights into why errors occur based on code analysis.43  
* **Suggesting Fixes:** Generating potential code corrections for identified issues.43  
* **Generating Tests:** Creating unit tests based on existing code to verify functionality and catch regressions.43  
* **Generating Documentation/Comments:** Assisting with the creation of explanatory text for code.43  
* **Summarizing Changes:** Explaining the differences between code versions (diffs) or summarizing recent commits.67

These capabilities suggest a primary value proposition for AI lies in accelerating the human's mental model construction and reducing comprehension-related cognitive load—addressing the most time-consuming part of the development workflow.7

Furthermore, AI agents can be trained on the vast amounts of data generated by human developers, such as discussions on Stack Overflow 30, Hacker News threads on debugging 44, and GitHub issue threads.21 This data captures real-world problems, common errors, successful (and unsuccessful) debugging strategies, and the natural language dialogues surrounding them. Training on this data can help AI learn common bug patterns, relevant solutions, and even conversational interaction styles for debugging.

Research is moving towards agents that engage in multi-step reasoning, utilize external tools (like linters, compilers, debuggers), and interact with execution environments to iteratively diagnose and resolve issues, mirroring the human process more closely.21 The interaction patterns themselves—how an AI explains its reasoning, asks clarifying questions, or presents alternative hypotheses—can be designed based on effective human collaboration practices.24

### **5.3 Addressing Gaps: Aligning AI Capabilities with Real-World Developer Needs**

Despite progress, significant gaps remain between current AI capabilities and the full spectrum of challenges faced by human developers. AI agents still struggle with certain types of execution errors 21, and specialized domains like ML debugging remain poorly supported, with research addressing less than half of the identified practical challenges.19 This suggests a need for AI to better handle ambiguity, non-determinism, and the complex, often implicit, dependencies present in modern software systems.

Crucially, the design of AI development tools must be human-centered.7 For AI tools to be adopted and effective, they must align with developers' existing workflows, expectations, and mental models.16 A tool whose internal mechanisms or suggested outputs conflict with a developer's understanding can lead to confusion, mistrust, and reduced productivity.16 User feedback and empirical evaluation of usability are therefore critical.28

The introduction of AI assistance also changes the cognitive landscape for the developer. Studies show that while awareness of code provenance (knowing code was generated by AI) can lead to improved task performance (better validation and repair), it also increases the developer's cognitive workload.34 This suggests developers adopt a "trust but verify" stance, investing more mental effort in scrutinizing AI-generated code.34 This finding has two key implications: first, AI transparency and explainability are paramount to support this necessary validation process. Second, AI assistance shifts the developer's primary cognitive task from *creation* or *debugging* towards *supervision* and *validation* of AI output. This supervisory role carries its own cognitive demands that tool designers must consider. AI tools should not only generate suggestions but also provide features that facilitate efficient and effective validation by the human developer (e.g., highlighting uncertain sections, explaining rationale, linking to evidence).

Finally, developer concerns regarding AI tools, including security implications, ethical considerations (e.g., data privacy, bias), and reliability, must be addressed to foster trust and adoption.67

## **6\. Conclusion: Towards More Human-Centric AI Development Tools**

### **6.1 Synthesis of Human Strategies**

The exploration of human coding and debugging reveals a set of sophisticated cognitive strategies honed to manage the inherent complexity of software development. Key takeaways include:

* **Dynamic and Context-Aware Strategies:** Developers, especially experts, do not rely on fixed procedures but dynamically select and adapt comprehension and debugging strategies based on the specific context, including the nature of the task, the characteristics of the defect, their familiarity with the codebase, and the available tools.  
* **Centrality of Mental Models:** Effective interaction with code hinges on the construction and refinement of mental models—internal representations of the system's structure and behavior. These models are often partial, evolve over time, and are expensive to build and maintain.  
* **Cognitive Load Management:** Strategies like opportunistic comprehension and reliance on external aids are adaptations to manage the significant cognitive load imposed by development tasks and the limitations of human working memory.  
* **The External Mind:** Developers extensively use external cognitive aids—IDEs, notes, journals, diagrams, debugging documents, online resources—not just to store information but to actively structure their thinking, offload memory, track progress, and manage complex problem-solving processes.  
* **Iterative Problem-Solving:** Both coding and debugging are fundamentally iterative processes involving cycles of information gathering, hypothesis generation/refinement, action/experimentation, and evaluation.

### **6.2 Recommendations for AI Agent Design**

Translating these human strategies into effective AI software development agents requires moving beyond current paradigms. Based on the analysis, the following design principles are recommended:

1. **Model Cognitive Control Loops:** Focus on implementing the higher-level cognitive control mechanisms observed in experts—goal setting, context assessment, dynamic strategy selection (considering cost/benefit), hypothesis management, and iterative refinement—rather than just automating isolated actions.  
2. **Embed Context Awareness:** Equip agents with the ability to perceive and reason about contextual factors, such as codebase characteristics (size, complexity, language, familiarity metrics), defect types (error messages, reproducibility, location), task goals, and environment constraints, to inform strategy selection.  
3. **Implement Explicit External Reasoning:** Provide agents with structured mechanisms (analogous to journals or debugging docs) to log their reasoning steps, track hypotheses, record findings, and manage plans. This enhances transparency, robustness for complex tasks, and facilitates potential human oversight or collaboration.  
4. **Integrate Diverse Knowledge Sources:** Enable agents to ingest, process, and synthesize information from multiple sources beyond static code, including documentation (NLP), commit history, test results, execution traces, and potentially curated online knowledge bases (e.g., Stack Overflow).  
5. **Prioritize Explainability and Validation Support:** Design agents to clearly explain their reasoning, proposed changes, and confidence levels. Provide features that specifically support the human developer's role in validating AI suggestions, acknowledging the cognitive load involved in this supervisory task.  
6. **Address Specific Domain Challenges:** Target known gaps, such as the unique difficulties in debugging ML systems (probabilistic nature, data dependencies) and handling ambiguity or non-determinism more broadly.  
7. **Adopt Human-Centered Design:** Continuously evaluate AI tools against developer workflows, mental models, and usability metrics through empirical studies and user feedback to ensure alignment and foster trust and adoption.

### **6.3 Future Directions**

While this report synthesizes current understanding, the intersection of human cognition and AI in software development remains a fertile ground for research. Future work should focus on:

* **Empirical Studies of Human-AI Collaboration:** Conducting detailed observational and experimental studies of developers interacting with AI coding assistants to understand how collaboration unfolds, measure impacts on cognitive load, performance, and learning, and identify effective interaction patterns.  
* **Measuring Cognitive Impact:** Developing refined methods, potentially combining physiological measures (fNIRS, eye-tracking) with behavioral data, to quantify the cognitive load implications of different AI assistance features and interaction designs.  
* **AI for Higher-Level Cognition:** Exploring how AI can support more complex cognitive tasks beyond code generation and local debugging, such as architectural design, strategic refactoring, requirements analysis, and long-term project planning.  
* **Modeling Expertise Development:** Investigating how AI might not only assist but also facilitate the development of expertise in human programmers, perhaps through adaptive scaffolding or targeted explanations.

By continuing to draw inspiration from the sophisticated cognitive processes of human developers, the field can strive towards creating AI tools that are not just powerful, but truly synergistic partners in the complex craft of software engineering.

#### **Obras citadas**

1. (PDF) Expert problem solving strategies for program comprehension \- ResearchGate, fecha de acceso: abril 25, 2025, [https://www.researchgate.net/publication/221518132\_Expert\_problem\_solving\_strategies\_for\_program\_comprehension](https://www.researchgate.net/publication/221518132_Expert_problem_solving_strategies_for_program_comprehension)  
2. Cognitive Aspects of Software Engineering, fecha de acceso: abril 25, 2025, [http://www.agentlab.de/cognitive\_aspects.html](http://www.agentlab.de/cognitive_aspects.html)  
3. From anecdote to evidence: the relationship between personality and need for cognition of developers \- PubMed Central, fecha de acceso: abril 25, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8928712/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8928712/)  
4. How to Improve Logic Building in Coding? 9 Easy Steps To Follow \- Softspace Solutions, fecha de acceso: abril 25, 2025, [https://softspacesolutions.com/blog/how-to-improve-logic-building-in-coding/](https://softspacesolutions.com/blog/how-to-improve-logic-building-in-coding/)  
5. Why I Love Coding | Henrik Warne's blog, fecha de acceso: abril 25, 2025, [https://henrikwarne.com/2012/06/02/why-i-love-coding/](https://henrikwarne.com/2012/06/02/why-i-love-coding/)  
6. 12 Essential Habits To Learn To Become A Professional Software Developer \- Unosquare, fecha de acceso: abril 25, 2025, [https://www.unosquare.com/blog/12-essential-habits-to-learn-to-become-a-professional-software-developer/](https://www.unosquare.com/blog/12-essential-habits-to-learn-to-become-a-professional-software-developer/)  
7. Human-Centered Approach to Static-Analysis-Driven Developer Tools, fecha de acceso: abril 25, 2025, [https://cacm.acm.org/practice/human-centered-approach-to-static-analysis-driven-developer-tools/](https://cacm.acm.org/practice/human-centered-approach-to-static-analysis-driven-developer-tools/)  
8. Maintaining Mental Models: A Study of Developer Work Habits \- GMU CS Department, fecha de acceso: abril 25, 2025, [https://cs.gmu.edu/\~tlatoza/papers/icse2006.pdf](https://cs.gmu.edu/~tlatoza/papers/icse2006.pdf)  
9. Developers' Visuo-spatial Mental Model and Program Comprehension \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/pdf/2304.09301](https://arxiv.org/pdf/2304.09301)  
10. Using CognitIDE to Capture Developers' Cognitive Load via Physiological Activity During Everyday Software Development Tasks The work of Fabian Stolp is funded by the Hasso Plattner Institute Research School on Data Science and Engineering. Charlotte Brandebusemeyer's work is funded by the SAP \- HPI Research Program. \*Both authors contributed equally. \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/html/2503.03537v1](https://arxiv.org/html/2503.03537v1)  
11. Towards a Fine-grained Analysis of Cognitive Load During Program Comprehension \- Alexandria (UniSG), fecha de acceso: abril 25, 2025, [https://www.alexandria.unisg.ch/bitstreams/511233e1-3e2a-4ad1-bf03-37eb59fe4fc0/download](https://www.alexandria.unisg.ch/bitstreams/511233e1-3e2a-4ad1-bf03-37eb59fe4fc0/download)  
12. Moving towards Objective Measures of Program Comprehension, fecha de acceso: abril 25, 2025, [https://par.nsf.gov/servlets/purl/10090362](https://par.nsf.gov/servlets/purl/10090362)  
13. Studying Developer Eye Movements to Measure Cognitive Workload and Visual Effort for Expertise Assessment \- DigitalCommons@UNL, fecha de acceso: abril 25, 2025, [https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1347\&context=csearticles](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1347&context=csearticles)  
14. Program Comprehension: Past, Present, and Future \- Infosun, fecha de acceso: abril 25, 2025, [https://www.infosun.fim.uni-passau.de/cl/publications/docs/FoSE16.pdf](https://www.infosun.fim.uni-passau.de/cl/publications/docs/FoSE16.pdf)  
15. The Effect of Poor Source Code Lexicon and Readability on Developers' Cognitive Load | Venera Arnaoudova, fecha de acceso: abril 25, 2025, [https://veneraarnaoudova.ca/wp-content/uploads/2018/03/2018-ICPC-Effect-lexicon-cognitive-load.pdf](https://veneraarnaoudova.ca/wp-content/uploads/2018/03/2018-ICPC-Effect-lexicon-cognitive-load.pdf)  
16. Understanding User Mental Models in AI-Driven Code Completion Tools: Insights from an Elicitation Study \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/html/2502.02194v1](https://arxiv.org/html/2502.02194v1)  
17. Code Like a Pro: Mental Models for Dev Success \- Howdy, fecha de acceso: abril 25, 2025, [https://www.howdy.com/blog/code-like-a-pro-mental-models-for-dev-success](https://www.howdy.com/blog/code-like-a-pro-mental-models-for-dev-success)  
18. Mental Models: Ultimate Guide To Make Intelligent Decisions \- LambdaTest, fecha de acceso: abril 25, 2025, [https://www.lambdatest.com/learning-hub/mental-models](https://www.lambdatest.com/learning-hub/mental-models)  
19. A Systematic Survey on Debugging Techniques for Machine Learning Systems \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/html/2503.03158v1](https://arxiv.org/html/2503.03158v1)  
20. \[2503.03158\] A Systematic Survey on Debugging Techniques for Machine Learning Systems \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/abs/2503.03158](https://arxiv.org/abs/2503.03158)  
21. Unveiling Pitfalls: Understanding Why AI-driven Code Agents Fail at GitHub Issue Resolution \- arXiv, fecha de acceso: abril 25, 2025, [https://www.arxiv.org/pdf/2503.12374](https://www.arxiv.org/pdf/2503.12374)  
22. Reviewing Strategies Seen Through Code Comprehension Theories \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/html/2503.21455v1](https://arxiv.org/html/2503.21455v1)  
23. Synthesizing Research on Programmers' Mental Models of Programs, Tasks and Concepts \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/pdf/2212.07763](https://arxiv.org/pdf/2212.07763)  
24. How Agile Practices Influence the Performance of Software Development Teams: The Role of Shared Mental Models and Backup, fecha de acceso: abril 25, 2025, [https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1210\&context=icis2014](https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1210&context=icis2014)  
25. Maintaining Mental Models: A Study of Developer Work Habits \- ResearchGate, fecha de acceso: abril 25, 2025, [https://www.researchgate.net/publication/200086098\_Maintaining\_Mental\_Models\_A\_Study\_of\_Developer\_Work\_Habits](https://www.researchgate.net/publication/200086098_Maintaining_Mental_Models_A_Study_of_Developer_Work_Habits)  
26. How to Understand a Large Codebase \- Sparkbox, fecha de acceso: abril 25, 2025, [https://sparkbox.com/foundry/how\_to\_understand\_a\_large\_codebase](https://sparkbox.com/foundry/how_to_understand_a_large_codebase)  
27. How to Understand a Large Codebase Like a Pro \- DEV Community, fecha de acceso: abril 25, 2025, [https://dev.to/jitendrachoudhary/how-to-understand-a-large-codebase-like-a-pro-hmb](https://dev.to/jitendrachoudhary/how-to-understand-a-large-codebase-like-a-pro-hmb)  
28. (PDF) Toward a Theory of Programming Language and Reasoning Assistant Design: Minimizing Cognitive Load \- ResearchGate, fecha de acceso: abril 25, 2025, [https://www.researchgate.net/publication/355225320\_Toward\_a\_Theory\_of\_Programming\_Language\_and\_Reasoning\_Assistant\_Design\_Minimizing\_Cognitive\_Load](https://www.researchgate.net/publication/355225320_Toward_a_Theory_of_Programming_Language_and_Reasoning_Assistant_Design_Minimizing_Cognitive_Load)  
29. arxiv.org, fecha de acceso: abril 25, 2025, [https://arxiv.org/pdf/2501.11792](https://arxiv.org/pdf/2501.11792)  
30. Debugging with Stack Overflow: Web Search Behavior in Novice and Expert Programmers \- University of Michigan, fecha de acceso: abril 25, 2025, [https://public.websites.umich.edu/\~endremad/papers/SODebug2022.pdf](https://public.websites.umich.edu/~endremad/papers/SODebug2022.pdf)  
31. An Initial Study to Develop an Empirical Test for Software Engineering Expertise, fecha de acceso: abril 25, 2025, [https://www.researchgate.net/publication/228971739\_An\_Initial\_Study\_to\_Develop\_an\_Empirical\_Test\_for\_Software\_Engineering\_Expertise](https://www.researchgate.net/publication/228971739_An_Initial_Study_to_Develop_an_Empirical_Test_for_Software_Engineering_Expertise)  
32. An Initial Study to Develop an Empirical Test for Software Engineering Expertise \- CiteSeerX, fecha de acceso: abril 25, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=fc38c0fa62582b0aea33e131475c7ecfc6af3abe](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=fc38c0fa62582b0aea33e131475c7ecfc6af3abe)  
33. Supporting Code Comprehension via Annotations: Right Information at the Right Time and Place, fecha de acceso: abril 25, 2025, [https://web.engr.oregonstate.edu/\~sarmaa/wp-content/uploads/2020/08/vlhcc20-adeli.pdf](https://web.engr.oregonstate.edu/~sarmaa/wp-content/uploads/2020/08/vlhcc20-adeli.pdf)  
34. A Study on Developer Behaviors for Validating and Repairing LLM-Generated Code Using Eye Tracking and IDE Actions \- arXiv, fecha de acceso: abril 25, 2025, [https://arxiv.org/html/2405.16081v1](https://arxiv.org/html/2405.16081v1)  
35. Code Summarization for Opportunistic Reuse in Large Software Systems \- IIIT Hyderabad, fecha de acceso: abril 25, 2025, [https://web2py.iiit.ac.in/research\_centres/publications/download/phdthesis.pdf.b2c99344a9a9404c.5068442d5468657369732d4e617665656e4b756c6b61726e692d3230313039393030342d4669616e6c2e706466.pdf](https://web2py.iiit.ac.in/research_centres/publications/download/phdthesis.pdf.b2c99344a9a9404c.5068442d5468657369732d4e617665656e4b756c6b61726e692d3230313039393030342d4669616e6c2e706466.pdf)  
36. A Retrospective on How Developers Seek, Relate, and Collect ..., fecha de acceso: abril 25, 2025, [https://www.computer.org/csdl/journal/ts/2025/03/10855640/23QQWt3qUso](https://www.computer.org/csdl/journal/ts/2025/03/10855640/23QQWt3qUso)  
37. How I Debug Faster with These Simple Tricks \- DEV Community, fecha de acceso: abril 25, 2025, [https://dev.to/rowsanali/how-i-debug-faster-with-these-simple-tricks-l2h](https://dev.to/rowsanali/how-i-debug-faster-with-these-simple-tricks-l2h)  
38. Essential debugging techniques for developers \- Upsun, fecha de acceso: abril 25, 2025, [https://upsun.com/blog/debugging-techniques-for-developers/](https://upsun.com/blog/debugging-techniques-for-developers/)  
39. Coding Standards And Best Practices: Guide & Implementation Tips \- DevCom, fecha de acceso: abril 25, 2025, [https://devcom.com/tech-blog/coding-standards-and-best-practices-guide-implementation-tips/](https://devcom.com/tech-blog/coding-standards-and-best-practices-guide-implementation-tips/)  
40. What coding practices have you come to rely on in your career? \- Reddit, fecha de acceso: abril 25, 2025, [https://www.reddit.com/r/ExperiencedDevs/comments/14sv3rj/what\_coding\_practices\_have\_you\_come\_to\_rely\_on\_in/](https://www.reddit.com/r/ExperiencedDevs/comments/14sv3rj/what_coding_practices_have_you_come_to_rely_on_in/)  
41. Exploration and Visualization of Large Execution Traces \- Faculty of Engineering, fecha de acceso: abril 25, 2025, [https://www.site.uottawa.ca/\~tcl/gradtheses/lfu/LfuThesisJun30-2005Final.pdf](https://www.site.uottawa.ca/~tcl/gradtheses/lfu/LfuThesisJun30-2005Final.pdf)  
42. CodeWalk: Facilitating Shared Awareness in Mixed-Ability Collaborative Software Development \- Andrew Begel, fecha de acceso: abril 25, 2025, [https://andrewbegel.com/papers/assets-2022-potluri.pdf](https://andrewbegel.com/papers/assets-2022-potluri.pdf)  
43. How to debug code with GitHub Copilot, fecha de acceso: abril 25, 2025, [https://github.blog/ai-and-ml/github-copilot/how-to-debug-code-with-github-copilot/](https://github.blog/ai-and-ml/github-copilot/how-to-debug-code-with-github-copilot/)  
44. Thoughts on Debugging | Hacker News, fecha de acceso: abril 25, 2025, [https://news.ycombinator.com/item?id=41643319](https://news.ycombinator.com/item?id=41643319)  
45. Debugging: Indispensable rules for finding even the most elusive ..., fecha de acceso: abril 25, 2025, [https://news.ycombinator.com/item?id=42682602](https://news.ycombinator.com/item?id=42682602)  
46. How Do Elementary Students Apply Debugging Strategies in a Block-Based Programming Environment? \- MDPI, fecha de acceso: abril 25, 2025, [https://www.mdpi.com/2227-7102/15/3/292](https://www.mdpi.com/2227-7102/15/3/292)  
47. Troubleshooting: A skill that never goes obsolete \- Hacker News, fecha de acceso: abril 25, 2025, [https://news.ycombinator.com/item?id=43170843](https://news.ycombinator.com/item?id=43170843)  
48. Tutorial Learn to Debug an Issue Using a Debugging Doc · oppia ..., fecha de acceso: abril 25, 2025, [https://github.com/oppia/oppia/wiki/Tutorial-Learn-to-Debug-an-Issue-Using-a-Debugging-Doc](https://github.com/oppia/oppia/wiki/Tutorial-Learn-to-Debug-an-Issue-Using-a-Debugging-Doc)  
49. Debugging StackOverflow errors \- .NET \- Learn Microsoft, fecha de acceso: abril 25, 2025, [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-stackoverflow](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-stackoverflow)  
50. Debugging a Stack Overflow \- Windows drivers | Microsoft Learn, fecha de acceso: abril 25, 2025, [https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugging-a-stack-overflow](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugging-a-stack-overflow)  
51. Need advice: how do you build strong mental models of complex systems fast? \- Reddit, fecha de acceso: abril 25, 2025, [https://www.reddit.com/r/SoftwareEngineering/comments/17m0hte/need\_advice\_how\_do\_you\_build\_strong\_mental\_models/](https://www.reddit.com/r/SoftwareEngineering/comments/17m0hte/need_advice_how_do_you_build_strong_mental_models/)  
52. You should keep a developer's journal \- Stack Overflow, fecha de acceso: abril 25, 2025, [https://stackoverflow.blog/2024/12/24/you-should-keep-a-developer-s-journal/](https://stackoverflow.blog/2024/12/24/you-should-keep-a-developer-s-journal/)  
53. Tips And Strategies For Note-Taking In Computer Science ..., fecha de acceso: abril 25, 2025, [https://codingzap.com/strategies-for-note-taking-in-computer-science/](https://codingzap.com/strategies-for-note-taking-in-computer-science/)  
54. The Best Note-Taking Methods: How To Take Notes in 2025?, fecha de acceso: abril 25, 2025, [https://www.sembly.ai/blog/the-best-note-taking-methods-and-types/](https://www.sembly.ai/blog/the-best-note-taking-methods-and-types/)  
55. The 8 Best Note-Taking Tools for Project Managers in 2024 \- Salina, fecha de acceso: abril 25, 2025, [https://salina.app/blog/best-note-taking-tools-for-project-managers/](https://salina.app/blog/best-note-taking-tools-for-project-managers/)  
56. How to Write Good Code: 10 Beginner-friendly Techniques for Instant Results \- SitePoint, fecha de acceso: abril 25, 2025, [https://www.sitepoint.com/how-to-write-good-code/](https://www.sitepoint.com/how-to-write-good-code/)  
57. Programming Routine: 10 Better Habits Web Developers Should Embrace, fecha de acceso: abril 25, 2025, [https://www.apollotechnical.com/better-habits-web-developers-should-embrace/](https://www.apollotechnical.com/better-habits-web-developers-should-embrace/)  
58. Effective Strategies for Refactoring a Large Codebase: Best Practices and Approaches, fecha de acceso: abril 25, 2025, [https://dev.to/adityabhuyan/effective-strategies-for-refactoring-a-large-codebase-best-practices-and-approaches-1bpj](https://dev.to/adityabhuyan/effective-strategies-for-refactoring-a-large-codebase-best-practices-and-approaches-1bpj)  
59. What are good coding habits to have from the start? : r/webdev \- Reddit, fecha de acceso: abril 25, 2025, [https://www.reddit.com/r/webdev/comments/154bda0/what\_are\_good\_coding\_habits\_to\_have\_from\_the\_start/](https://www.reddit.com/r/webdev/comments/154bda0/what_are_good_coding_habits_to_have_from_the_start/)  
60. The Importance of Sketching with Code \- Gorilla Sun, fecha de acceso: abril 25, 2025, [https://www.gorillasun.de/blog/the-importance-of-sketching-with-code/](https://www.gorillasun.de/blog/the-importance-of-sketching-with-code/)  
61. What does a good programmer's code look like? \[closed\] \- Stack Overflow, fecha de acceso: abril 25, 2025, [https://stackoverflow.com/questions/366588/what-does-a-good-programmers-code-look-like](https://stackoverflow.com/questions/366588/what-does-a-good-programmers-code-look-like)  
62. 15 Essential Habits for New Programmers to Cultivate Success – AlgoCademy Blog, fecha de acceso: abril 25, 2025, [https://algocademy.com/blog/15-essential-habits-for-new-programmers-to-cultivate-success/](https://algocademy.com/blog/15-essential-habits-for-new-programmers-to-cultivate-success/)  
63. Productive R workflow, fecha de acceso: abril 25, 2025, [https://www.productive-r-workflow.com/](https://www.productive-r-workflow.com/)  
64. Software development workflow and productivity : r/softwaredevelopment \- Reddit, fecha de acceso: abril 25, 2025, [https://www.reddit.com/r/softwaredevelopment/comments/183fedd/software\_development\_workflow\_and\_productivity/](https://www.reddit.com/r/softwaredevelopment/comments/183fedd/software_development_workflow_and_productivity/)  
65. 6 Practices for Effective Pull Requests \- Pete Hodgson, fecha de acceso: abril 25, 2025, [https://blog.thepete.net/blog/2019/05/10/6-practices-for-effective-pull-requests/](https://blog.thepete.net/blog/2019/05/10/6-practices-for-effective-pull-requests/)  
66. Guide to Conquering Spaghetti Code \- Iterators, fecha de acceso: abril 25, 2025, [https://www.iteratorshq.com/blog/guide-to-conquering-spaghetti-code/](https://www.iteratorshq.com/blog/guide-to-conquering-spaghetti-code/)  
67. The State of Developer Ecosystem in 2023 Infographic | JetBrains ..., fecha de acceso: abril 25, 2025, [https://www.jetbrains.com/lp/devecosystem-2023/](https://www.jetbrains.com/lp/devecosystem-2023/)