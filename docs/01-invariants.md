# System Invariants

## Purpose

This document defines the non-negotiable correctness constraints of the system.

If any invariant is violated, the system is considered broken.

Invariants apply across:
- retrieval
- planning
- execution
- memory
- generation
- observability

They are implementation-agnostic and must hold regardless of model, stack, or architecture.

---

## 01. Evidence-Bound Claims

**Statement**

* Every factual claim in a generated answer must be representable as an addressable Claim and must be supported by either retrieved evidence or an explicitly declared parametric knowledge boundary recorded at decision time.

**Applies To**

* Generation layer
* Retrieval layer
* Planning layer
* Observability layer

**Violation Condition**

* A generated answer contains a factual assertion that (a) cannot be identified as a Claim, or (b) cannot be traced to retrieved evidence units or to a recorded decision explicitly permitting parametric knowledge use.

**Why This Exists**

* Prevents hallucinated or unsupported claims while allowing controlled and accountable use of parametric model knowledge.

## 02. Attributed Semantic Memory

**Statement**

* Semantic memory may only influence decisions if its source, timestamp, and scope are explicitly recorded and inspectable.

**Applies To**

* Memory layer
* Planning layer
* Generation layer
* Observability layer

**Violation Condition**

* A decision or answer is influenced by semantic memory that lacks source attribution or temporal metadata.

**Why This Exists**

* Prevents silent memory drift and authority inversion.

## 03. Memory Scope Integrity 

**Statement**

* Information may only persist across sessions if it is explicitly designated for long-term use and its scope is clearly defined.

**Applies To**

* Memory layer
* Planning layer
* Generation layer
* Observability layer

**Violation Condition**

* Session-scoped or incomplete information influences future decisions or answers beyond its intended context.

**Why This Exists**

* Prevents silent persistence of transient reasoning, incomplete thoughts, or context-specific assumptions.

## 04. Justified Retrieval Decision

**Statement**

* The system must not generate an answer unless the decision to retrieve or not retrieve is explicitly justified by recorded signals available at decision time.

**Applies To**

* Planning layer
* Generation layer
* Observability layer

**Violation Condition**

* An answer is generated without a recorded justification for whether retrieval was invoked or bypassed.

**Why This Exists**

* Prevents silent reliance on parametric knowledge and enforces accountable decision boundaries between retrieval and generation.

## 05. Accountable Generation Action

**Statement**

* The system must not answer, hedge, or refuse unless the specific signals that justified that action are recorded at decision time.

**Applies To**

* Policy layer
* Planning layer
* Generation layer
* Observability layer

**Violation Condition**

* A generation action (answer / hedge / refuse) occurs without a recorded set of sufficient signals that explain why that action was chosen over the alternatives.

**Why This Exists**

* Prevents opaque generation behavior and eliminates post-hoc rationalization of system decisions.

## 06. Layer-Isolated Evaluation

**Statement**

* Retrieval correctness must be assessable independently of generation behavior.

**Applies To**

* Retrieval layer
* Evaluation layer
* Observability layer

**Violation Condition**

* Retrieval quality is inferred solely from final answer correctness without isolating retrieval-layer signals.

**Why This Exists**

* Prevents misattribution of system failures and enforces proper layer-wise debugging.

## 07. Model-Agnostic Guarantees

**Statement**

* All system invariants must remain enforceable and verifiable regardless of the underlying language model.

**Applies To**

* All layers

**Violation Condition**

* A model upgrade causes any system invariant to become unenforceable, unverifiable, or silently violated.

**Why This Exists**

* Prevents model-specific behavior from undermining system correctness boundaries.

## 8. No Silent Invariant Violations

**Statement**

* The system must not produce a final answer if any invariant violation has occurred without explicitly surfacing an error state.

**Applies To**

* All layers

**Violation Condition**

* An invariant is violated and the system proceeds to generate a normal answer without signaling the violation.

**Why This Exists**

* Prevents silent corruption and ensures system failures are surfaced rather than masked.

## 9. Causal Trace Availability

**Statement**

* For every final answer, the system must retain sufficient decision-time signals to reconstruct the causal chain that led to it.

**Applies To**

* All layers

**Violation Condition**

* A final answer cannot be causally reconstructed from recorded decision-time signals.

**Why This Exists**

* Prevents opaque system behavior and eliminates post-hoc rationalization of decisions.

## 10. Evidence-Calibrated Confidence

**Statement**

* The system must not express confidence in a claim beyond what is justified by the strength and completeness of its recorded supporting signals.

**Applies To**

* Generation layer
* Policy layer
* Observability layer

**Violation Condition**

* A generated answer conveys certainty or authority that exceeds the strength, coverage, or consistency of the supporting evidence and decision-time signals.

**Why This Exists**

* Prevents confidence inflation and ensures the system’s expressed certainty is proportionate to its evidential support.