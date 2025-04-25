# Test Case Generation Guide & Definition of Done

**Goal:** Ensure comprehensive testing by considering standard scenarios, edge cases, and error conditions for each automation entity and the overall process flow. This guide replaces a simple DoD checklist with prompts for thorough test case design.

---

## I. General Test Considerations (Apply to most entities)

*   **Requirement Traceability:** Does every test case clearly map back to a requirement in `project_prd.md` or a specific function of an entity in `automation_entities.md`?
*   **Positive Scenarios ("Happy Path"):** Does the entity/flow work correctly with valid, expected inputs and conditions?
*   **Negative Scenarios (Invalid Inputs):** How does the entity/flow handle incorrect data types, missing fields, out-of-range values, malformed structures (e.g., bad JSON/XML), empty inputs, null inputs?
*   **Error Handling & Resilience:**
    *   How are internal errors (e.g., exceptions in code) caught, logged, and handled? Does the system recover gracefully?
    *   How are failures in external dependencies (APIs, databases, file systems) handled? (e.g., timeouts, connection errors, 4xx/5xx responses). Are retries implemented where appropriate?
    *   Are specific, informative error messages generated?
*   **Security Considerations (If applicable):**
    *   Input sanitization to prevent injection attacks?
    *   Proper authentication/authorization checks?
    *   Handling of sensitive data?
*   **Performance & Scalability (Based on Non-Functional Requirements in PRD):**
    *   Response time under expected load?
    *   Resource utilization (CPU, memory, network)?
    *   Behavior with large data volumes or high request frequency?
*   **Logging & Monitoring:** Are critical steps, decisions, inputs, outputs, and errors logged effectively for debugging and monitoring?

---

## II. Entity-Specific Test Case Prompts

### A. Events (Input Triggers)

*   **Payload Validation:**
    *   Test with perfectly valid event payloads.
    *   Test with missing required fields.
    *   Test with extra, unexpected fields.
    *   Test with incorrect data types for fields.
    *   Test with null values for fields (if applicable).
    *   Test with empty strings/lists/objects where data is expected.
    *   Test with malformed overall structure (e.g., invalid JSON).
*   **Trigger Conditions:** If the event triggers specific containers/teams based on payload content, test all branching logic.
*   **Duplicate Events:** How are duplicate events handled (if detection is required)?
*   **Out-of-Order Events:** If event order matters, how are out-of-order events handled?

### B. Tools (Internal & Containerized)

*   **Input Validation:** (See Negative Scenarios under General) Apply specifically to the tool's expected input parameters/data.
*   **Output Validation:** Does the tool produce the correct output format and values for various valid inputs? Does it handle cases where no output should be generated?
*   **Dependency Handling:**
    *   (Internal): Correct handling of imports and utility functions?
    *   (Containerized): Correct interaction with container environment (env vars, file mounts)? Correct handling if dependencies *within* the container fail?
*   **Statefulness:** If the tool is stateful, test its behavior across multiple calls. Ensure proper state initialization and cleanup.
*   **Idempotency:** If the tool should be idempotent (safe to call multiple times with the same input), verify this behavior.

### C. Teams (Core Logic Units)

*   **Input/Output Validation:** (See Events & Tools) Apply rigorously to the Team's specific I/O contract.
*   **Business Logic:**
    *   Test all core logic paths and decision branches.
    *   Test boundary conditions for numerical calculations or data processing.
    *   Test scenarios defined by the PRD use cases.
*   **Interaction with Tools:** Test the Team's interaction with any Internal or Containerized Tools it uses. Mock tool failures to test the Team's error handling.
*   **Evaluation Logic (If applicable):** If there's an Evaluation Team, test its criteria and decision-making process thoroughly against outputs from the Execution Team.

### D. Containers (Orchestration Flows)

*   **Flow Logic & Sequencing:**
    *   Verify the correct sequence of Team/Tool calls for the "happy path".
    *   Test conditional branching within the flow (if any step's output determines the next step).
    *   Test error handling *between* steps (e.g., if Tool A fails, does the Container handle it correctly before calling Team B?).
*   **Data Transformation/Passing:** Verify that data is correctly passed and transformed between steps within the Container.
*   **Rollback/Compensation (If applicable):** If the flow involves transactions or requires compensation logic on failure, test these mechanisms.
*   **End-to-End Scenarios:** Test the complete flow from the initial trigger (often an Event) to the final output or state change, covering various input scenarios.
*   **Timeout Handling:** Does the Container handle timeouts if individual steps take too long?

---

## III. Definition of Done (Confirmation)

*Once test cases derived from the prompts above are created, executed, and passing:*

- [ ] **Test Coverage:** All major functional paths, common error conditions, and relevant edge cases (identified using sections I & II) are covered by automated or documented manual tests.
- [ ] **Test Results:** All defined tests are passing. Any failing tests have corresponding bug reports.
- [ ] **Requirement Fulfillment:** Functionality meets the requirements specified in `project_prd.md` as verified by tests.
- [ ] **Code Quality:** Code adheres to project standards (linting, style guides).
- [ ] **Documentation:** Relevant documentation (`READMEs`, docstrings, entity definitions) is updated to reflect the implemented functionality and its usage/behavior.
- [ ] **Deployment:** (If applicable) Successfully deployed to the target environment.
- [ ] **Peer Review:** (If applicable) Code and test cases have been reviewed.
