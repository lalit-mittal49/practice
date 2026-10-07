from src.models.schemas import IntakeState, SocratesSlot

INTAKE_SYSTEM_PROMPT = """You are a clinical intake assistant helping gather
a structured symptom history before a patient sees a clinician. You follow
the SOCRATES framework (Site, Onset, Character, Radiation, Associated
symptoms, Timing, Exacerbating/relieving factors, Severity).

You will be told which slots are already filled and which are missing. Pick
the SINGLE most clinically useful missing slot to ask about next given the
conversation so far, and phrase one natural, empathetic follow-up question
for it. Do not ask about multiple slots at once. Do not diagnose. Do not
decide the conversation is complete — that is determined separately."""


def build_intake_user_prompt(state: IntakeState) -> str:
    filled = "\n".join(f"- {slot.value}: {value}" for slot, value in state.filled_slots.items()) or "(none yet)"
    missing = ", ".join(s.value for s in state.missing_slots())
    history = "\n".join(f"{turn['role']}: {turn['content']}" for turn in state.conversation_log[-6:])

    return f"""Chief complaint: {state.chief_complaint}

Already gathered:
{filled}

Missing slots: {missing}

Recent conversation:
{history}

Choose the best missing slot to ask about next and phrase the question."""


MARKER_EXTRACTION_SYSTEM_PROMPT = """You extract structured lab test results
from noisy OCR'd text. Extract every numeric lab marker you can identify as
a {test_name, value, unit} triple. Use standardized test names (e.g.
"Fasting Glucose" not "FBS" or "Fasting Blood Sugar" — normalize to the
standard name). Only extract values you can clearly identify — do not guess
a value for a test name that's mentioned without a clear associated number.
Do not classify or interpret the values — extraction only."""


def build_marker_extraction_prompt(raw_text: str) -> str:
    return f"""Extract all lab markers from this OCR'd report text:

---
{raw_text}
---

Return every {{test_name, value, unit}} triple you can identify."""
