# `Reference Architecture`

## Purpose

This document defines the canonical interaction model of system primitives under invariant constraints.

It describes:

* how primitives interact,
* when decisions occur,
* where invariant enforcement happens,
* and which state transitions are permitted or forbidden.

This is not a deployment architecture, infrastructure diagram, or implementation guide.

It is a **conceptual execution model** that remains valid regardless of:

* programming language,
* model provider,
* storage backend,
* orchestration framework.

[`01-invariants.md`](https://github.com/Arnav-Ajay/agentic-systems-blueprint/blob/main/docs/01-invariants.md) defines what must always be true,
[`02-system-primitives.md`](https://github.com/Arnav-Ajay/agentic-systems-blueprint/blob/main/docs/02-system-primitives.md) defines what must exist,

this document defines:

> How the system must behave in order to remain constitutionally valid.

---

## Design Principles

The reference architecture adheres to the following principles:

### 1. Invariant-First Execution

No phase of execution may proceed unless all applicable invariants remain satisfiable at that stage.

Invariant enforcement is structural, not retrospective.

---

### 2. Explicit State Transitions

All transitions between phases must be mediated by recorded Decisions and Signals.

No implicit transitions are permitted.

---

### 3. Query-Scoped Accountability

All actions, signals, claims, memory interactions, and confidence expressions must be traceable to a specific Query.

There is no global or anonymous behavior.

---

### 4. Separation of Reasoning and Commitment

Internal reasoning may occur, but externally visible actions (Generation Action, Memory Write, Error State) must be explicitly committed and recorded.

---

### 5. Detectable Failure Over Silent Corruption

If any invariant becomes unsatisfiable during execution, the system must transition to an explicit error state rather than emit a normal answer.

---

## Topics Covered in This Document

This reference architecture will define:

1. Canonical execution phases
2. Permitted primitive interactions
3. Decision boundaries and state transitions
4. Claim construction and grounding enforcement
5. Confidence calibration placement
6. Memory interaction boundaries
7. Invariant enforcement points
8. Illegal execution flows
9. Minimal valid system configuration

---

## Architectural Scope

This document intentionally excludes:

* API design
* Infrastructure topology
* Storage implementation
* Model configuration details
* Performance optimizations
* Tooling or framework choices

It focuses strictly on structural correctness and invariant preservation.

---

## Canonical Execution Flow

### Phase 1 - Query Initialization

**Objective**

Establish a uniquely identifiable execution boundary for the incoming query.

**Flow**

1. A Query primitive is instantiated.
2. A unique identifier is assigned.
3. Execution scope is defined (session, policy constraints, memory access boundaries).
4. A Trace Record is initialized and bound to the Query.
5. Initial Signals may be derived (e.g., query metadata, session state).
6. Query is registered as the active execution scope.

**Invariants Enforced**

* Invariant 09 (Causal Trace Availability)
* Invariant 03 (Memory Scope Integrity)

**Illegal Transitions**

* Proceeding to planning or generation without an instantiated Query and initialized Trace Record.

---

### Phase 2 - Planning & Retrieval Decision

**Objective**

Determine whether retrieval is required before generation.

**Flow**

1. Available Signals are gathered:
   * Query complexity
   * Policy constraints
   * Memory references (if allowed)
2. A Decision is recorded:
   * Retrieve OR bypass retrieval
3. Decision must include:
   * Signals considered
   * Explicit justification

**Invariant Enforcement**

* Invariant 04 (Justified Retrieval Decision)
* Invariant 09 (Causal Trace Availability)

**Illegal Transition**

* Generating output without a recorded retrieval decision.

---

### Phase 3 - Evidence Acquisition

**Objective**

Acquire retrievable information and evaluate its sufficiency for answering the Query.

**Flow**

1. If retrieval was selected in Phase 2, evidence acquisition is performed.
2. If retrieval was bypassed, this phase records explicit parametric reliance signals.
3. Retrieval Signals are recorded (e.g., similarity scores, coverage metrics).
4. A Decision is recorded:
   * Evidence sufficient
   * Evidence insufficient
   * Evidence conflicting
5. Evidence Units are attached to the Trace Record.

**Invariants Enforced**

* Invariant 06 (Layer-Isolated Evaluation)
* Invariant 09 (Causal Trace Availability)

**Illegal Transitions**

* Proceeding to generation without recording an evidence sufficiency decision when retrieval was invoked.

---

### Phase 4 - Generation Decision

**Objective**

Determine the appropriate generation action (answer / hedge / refuse / error) based on evidence sufficiency, policy constraints, and recorded signals.

**Flow**

1. Review evidence sufficiency decision from Phase 3.
2. Review policy constraints (confidence thresholds, safety constraints, grounding rules).
3. Gather relevant Signals (retrieval strength, conflict signals, memory influence, etc.).
4. Record a Decision selecting one of:
   * Answer
   * Hedge
   * Refuse
   * Error
5. Decision must include:
   * Signals considered
   * Rejected alternatives
   * Explicit justification

**Invariants Enforced**

* Invariant 05 (Accountable Generation Action)
* Invariant 08 (No Silent Invariant Violations)
* Invariant 09 (Causal Trace Availability)

**Illegal Transitions**

* Emitting output without a recorded generation decision.
* Selecting “Answer” when evidence is explicitly marked insufficient without recorded justification.

---

### Phase 5 - Output Construction and Claim Formation

**Objective**

Construct a candidate response and instantiate Claims from the candidate output.

**Flow**

1. Generation Action produces candidate output.
2. Output is segmented into Claims.
3. Each Claim is persisted as an addressable unit and linked to the Query + Generation Action.

**Invariants Enforced**

* Invariant 09 (Causal Trace Availability)

**Illegal Transitions**

* Producing output without Claims when the system is in “answer” mode.

---

### Phase 6 - Claim Grounding and Validation

**Objective**

Ensure all asserted claims are addressable and grounded.

**Flow**

1. Each Claim is assigned:
   * Evidence Unit references OR
   * Explicit parametric justification reference.
2. Unsupported claims are flagged.
3. If unsupported claims exist:
   * A Decision is recorded selecting the remediation path (regenerate / hedge / refuse / error).

**Invariant Enforcement**

* Invariant 01 (Evidence-Bound Claims)
* Invariant 08 (No Silent Invariant Violations)
* Invariant 10 (Evidence-Calibrated Confidence)

**Illegal Transition**

* Emitting final output containing a Claim without support mapping.
* Continuing to output release after any unsupported claim is detected, without switching to hedge/refuse/error.

---

### Phase 7 — Confidence Calibration

**Objective**

Assign and record a Confidence Expression that is proportionate to the strength, completeness, and consistency of supporting signals and grounded Claims.

**Flow**

1. Supporting Signals for each Claim are evaluated (evidence coverage, conflict signals, memory influence strength, etc.).
2. Overall evidential strength and consistency are assessed.
3. A Confidence Expression is instantiated and linked to:

   * The associated Generation Action
   * The associated Query
   * Supporting Signals
4. The expressed confidence level must not exceed evidential strength.
5. Confidence modality is selected:

   * Explicit confidence level (e.g., score or category), OR
   * Hedged language, OR
   * Refusal/error (if confidence cannot be justified).

**Invariants Enforced**

* Invariant 10 (Evidence-Calibrated Confidence)
* Invariant 05 (Accountable Generation Action)
* Invariant 09 (Causal Trace Availability)

**Illegal Transitions**

* Assigning high confidence when evidence is insufficient or conflicting.
* Emitting output without a recorded Confidence Expression (when in answer mode).
* Allowing tone or certainty to exceed recorded signal strength.

---

### Phase 8 — Trace Finalization & Output Release

**Objective**

Finalize the Trace Record and ensure all invariants remain satisfied before externally releasing the system outcome.

**Flow**

1. Verify that all Decisions, Signals, Claims, Memory interactions, and Confidence Expressions are linked to the Query.
2. Perform invariant validation check:

   * No unsupported Claims exist.
   * No unrecorded Decisions occurred.
   * No unresolved invariant violations remain.
3. If any invariant violation is detected:

   * Transition to recorded error state (Generation Action = error).
4. Finalize and persist the immutable Trace Record.
5. Release the externally visible system outcome.

**Invariants Enforced**

* Invariant 08 (No Silent Invariant Violations)
* Invariant 09 (Causal Trace Availability)
* All invariants implicitly verified at release boundary

**Illegal Transitions**

* Releasing output while invariant violations remain unresolved.
* Releasing output without a finalized Trace Record.
* Mutating Trace Record after output release.

---