# `System Primitives`

## Purpose of This File

This document defines the minimal conceptual objects required for the system invariants to be enforceable.

If a primitive does not exist, at least one invariant cannot be guaranteed.

Primitives are:

* implementation-agnostic
* model-agnostic
* storage-agnostic
* transport-agnostic

They are the irreducible building blocks of the system.

---

## What Counts as a Primitive?

A primitive is something like:

* Query
* Evidence Unit
* Decision
* Signal
* Memory Record
* Generation Action
* Trace Record
* Invariant State
* Claim
* Confidence Expression

If removing it would make one of your invariants impossible to enforce, it’s a primitive.

If removing it just makes implementation harder, it’s not.

---
## Primitives

### 01. Query

**Definition**

A uniquely identifiable unit of system input that defines the scope of reasoning, decision-making, and invariant enforcement.

**Required Properties**

* Unique identifier
* Input payload
* Time of receipt
* Session association (if any)
* Execution scope boundary

**Why It Exists**

Required to scope decision-making, trace reconstruction, and invariant enforcement to a bounded unit of execution.

### 02. Evidence Unit

**Definition**

An atomic, addressable unit of retrievable information that may be used to support a factual claim.

**Required Properties**

* Unique identifier
* Content payload
* Source attribution
* Retrieval context metadata

**Why It Exists**

Required to enforce:

* Evidence-Bound Claims
* Layer-Isolated Evaluation
* Causal Trace Availability

Without an addressable evidence unit, factual grounding cannot be verified.

---

### 03. Decision

**Definition**

A recorded selection among mutually exclusive system actions made at a specific point in time.

**Required Properties**

* Decision timestamp
* Decision type (e.g., retrieve, answer, refuse, write memory)
* Available signals at decision time
* Chosen action
* Rejected alternatives

**Why It Exists**

Required to enforce:

* Justified Retrieval Decision
* Accountable Generation Action
* Causal Trace Availability

Without a formal decision primitive, justification and accountability cannot be enforced.

### 04. Signal

**Definition**

A discrete, decision-time piece of information available to the system that may influence or justify a decision.

**Required Properties**

* Origin (e.g., retrieval, memory, policy evaluation, model output)
* Timestamp
* Associated query identifier
* Value or structured payload
* Confidence or strength indicator (if applicable)

**Why It Exists**

Required to enforce:
* Justified Retrieval Decision
* Accountable Generation Action
* Causal Trace Availability
* Evidence-Calibrated Confidence

Without a formal Signal primitive, decisions cannot be justified, causal chains cannot be reconstructed, and confidence cannot be calibrated against recorded evidence.

### 05. Memory Record

**Definition**

A persistent, addressable unit of stored information that may influence future system decisions beyond the originating query scope.

**Required Properties**

* Unique identifier
* Memory classification (e.g., semantic, episodic, working)
* Creation timestamp
* Originating query reference
* Recorded justification for persistence
* Intended scope of influence
* Content payload

**Why It Exists**

Required to enforce
* Attributed Semantic Memory
* Memory Scope Integrity
* Causal Trace Availability

Without a formal Memory Record primitive, persistent influence over future decisions cannot be governed, attributed, or bounded.

### 06. Generation Action

**Definition**

A committed system action representing the selected generation outcome (answer, hedge, or refuse) for a specific query.

**Required Properties**

* Unique identifier
* Associated query reference
* Action type (answer / hedge / refuse / error)
* Associated decision record
* Set of sufficient decision-time signals

**Why It Exists**

Required to enforce
* Accountable Generation Action
* Evidence-Calibrated Confidence
* Causal Trace Availability
* No Silent Invariant Violations

Without a formal Generation Action primitive, the system cannot distinguish between reasoning and committed output, nor justify why a specific outcome was selected.

### 07. Trace Record

**Definition**

An immutable, query-scoped record that captures the complete causal chain of signals, decisions, memory interactions, and actions leading to a final outcome.

**Required Properties**
* Unique identifier
* Associated query reference
* References to all relevant decision records
* References to all decision-time signals
* References to memory reads and writes
* References to generation actions
* Final outcome reference

**Why It Exists**

Required to enforce
* Causal Trace Availability
* No Silent Invariant Violations
* Justified Retrieval Decision
* Accountable Generation Action

Without a formal Trace Record primitive, the system cannot reconstruct, audit, or verify the causal chain that produced a given answer.

### 08. Claim

**Definition**

A minimal, addressable unit of asserted information in the system’s output that requires grounding (evidence-bound or explicitly permitted parametric).

**Required Properties**
* Unique identifier
* Associated query reference
* Associated generation action reference
* Claim text (or structured claim payload)
* Claim type (factual / numeric / definitional / recommendation / other)
* Support mapping references (evidence units and/or explicit parametric permission decision)
* Support status (supported / partially supported / unsupported)

**Why It Exists**

Required to enforce:
* Evidence-Bound Claims
* Causal Trace Availability
* Evidence-Calibrated Confidence

Without a Claim primitive, grounding cannot be verified at granular level and the system cannot reliably detect partial hallucinations within an otherwise “good” answer.

### 09. Confidence Expression

**Definition**

A structured representation of the system’s expressed certainty associated with a generated outcome.

**Required Properties**

* Associated generation action reference
* Associated query reference
* Confidence level or calibration descriptor
* Supporting signal references
* Expression modality (explicit score, hedged language, categorical level, etc.)

**Why It Exists**

Required to enforce:
* Evidence-Calibrated Confidence
* Accountable Generation Action
* Causal Trace Availability

Without a formal Confidence Expression primitive, the system cannot govern, calibrate, or audit the certainty conveyed in its responses.

## Primitive → Invariant Coverage

| Primitive             | Invariants Enforced |
| --------------------- | ------------------- |
| Query                 | 01, 03, 04, 05, 09  |
| Evidence Unit         | 01, 06, 09          |
| Claim                 | 01, 09, 10          |
| Decision              | 01, 04, 05, 09      |
| Signal                | 04, 05, 09, 10      |
| Memory Record         | 02, 03, 09          |
| Generation Action     | 05, 08, 09, 10      |
| Trace Record          | 04, 05, 08, 09      |
| Confidence Expression | 10, 05, 09          |