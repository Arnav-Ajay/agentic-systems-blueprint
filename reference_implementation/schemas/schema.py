# agentic_systems_bluebrint/reference_architecture/schemas/schema.py
# Schema definitions for the reference implementation.

from dataclasses import dataclass
from typing import List, Optional
import enum
from datetime import datetime, field

class signal_type_enum(enum.Enum):
    RETRIEVAL = "retrieval"
    MEMORY = "memory"
    POLICY_EVALUATION = "policy_evaluation"
    MODEL_OUTPUT = "model_output"

class decision_type_enum(enum.Enum):
    RETRIEVAL_DECISION = "retrieval_decision"
    EVIDENCE_SUFFICIENCY_DECISION = "evidence_sufficiency_decision"
    GENERATION_DECISION = "generation_decision"
    MEMORY_WRITE_DECISION = "memory_write_decision"

class action_type_enum(enum.Enum):
    ANSWER = "answer"
    HEDGE = "hedge"
    REFUSE = "refuse"
    ERROR = "error"

class memory_classification_enum(enum.Enum):
    SEMANTIC = "semantic"
    EPISODIC = "episodic"
    WORKING = "working"

class claim_type_enum(enum.Enum):
    FACTUAL = "factual"
    NUMERIC = "numeric"
    DEFINITIONAL = "definitional"
    RECOMMENDATION = "recommendation"
    OTHER = "other"

class support_status_enum(enum.Enum):
    SUPPORTED = "supported"
    PARTIALLY_SUPPORTED = "partially_supported"
    UNSUPPORTED = "unsupported"

# Query
@dataclass
class Query:
    query_id: str
    query_text: str
    ts_utc: datetime
    session_id: Optional[str] = None
    execution_scope: Optional[str] = None

# EvidenceUnit
@dataclass
class EvidenceUnit:
    evidence_id: str
    content: str
    source_attribution: Optional[str] = None
    retrieval_context_metadata: dict = field(default_factory=dict)

# Signal
@dataclass
class Signal:
    signal_id: str
    signal_type: signal_type_enum
    content_payload: str
    query_identifier: str
    ts_utc: datetime
    confidence_score: Optional[float] = None

# Decision
@dataclass
class Decision:
    decision_id: str
    decision_type: decision_type_enum
    ts_utc: datetime
    available_signal_refs: List[str]
    chosen_action: str  # but validated against decision_type at runtime
    rejected_alternatives: List[str]    
    justification: str

# Claim
@dataclass
class Claim:
    claim_id: str
    query_reference: str
    generation_action_reference: str
    claim_text: str
    claim_type: claim_type_enum
    support_mapping: List[str]  # evidence ids or parametric decision id
    support_status: support_status_enum

# GenerationAction
@dataclass
class GenerationAction:
    action_id: str
    action_type: action_type_enum
    ts_utc: datetime
    query_reference: str
    decision_reference: str

# MemoryRecord
@dataclass
class MemoryRecord:
    memory_id: str
    memory_classification: memory_classification_enum
    ts_utc: datetime
    query_reference: str
    justification_for_persistence: str
    intended_scope_of_influence: str
    content_payload: str

@dataclass
class InvariantState:
    invariant_id: str
    status: bool
    violation_reason: Optional[str]

# TraceRecord
@dataclass
class TraceRecord:
    record_id: str
    query_ref: str
    signal_refs: List[str]
    decision_refs: List[str]
    claim_refs: List[str]
    memory_read_write_refs: List[str]
    generation_action_ref: str
    confidence_expression_ref: Optional[str]
    invariant_states: List[InvariantState]
    final_outcome_reference: str

# ConfidenceExpression
@dataclass
class ConfidenceExpression:
    confidence_id: str
    confidence_score: float
    calibration_rationale: str
    query_reference: str
    generation_action_reference: str
    supporting_signal_references: List[str]
    expression_modality: str