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

# What Counts as a Primitive?

A primitive is something like:

* Query
* Evidence Unit
* Decision
* Signal
* Memory Record
* Generation Action
* Trace Record
* Invariant State
* Confidence Expression

If removing it would make one of your invariants impossible to enforce, it’s a primitive.

If removing it just makes implementation harder, it’s not.

---

## 01. Evidence Unit

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

## 02. Decision

**Definition**

A recorded selection among mutually exclusive system actions made at a specific point in time.

**Required Properties**

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

