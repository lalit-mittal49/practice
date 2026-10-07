"""
LLM client wrapper — the core GenAI-engineering piece of this project.

Both call sites in this codebase (next-question generation, marker
extraction) need the LLM to return DATA, not prose — so both go through
Gemini's structured output feature: passing a Pydantic model directly as
`response_schema` with `response_mime_type="application/json"` forces the
model to return JSON matching that exact shape. The raw JSON is still
re-validated with Pydantic before anything downstream trusts it — Gemini's
schema adherence is strong but not a substitute for validating the contract
yourself, especially across model/SDK versions.

This module is designed to run WITHOUT an API key: every public function
has a documented deterministic fallback, so the state-machine and
classification logic (the parts that matter for correctness) are fully
testable without any external dependency.
"""
from __future__ import annotations

from typing import TypeVar

from pydantic import BaseModel, ValidationError

from src.config import get_settings

T = TypeVar("T", bound=BaseModel)


class StructuredLLMError(Exception):
    pass


def call_structured(
    system_prompt: str,
    user_prompt: str,
    response_model: type[T],
    max_retries: int = 1,
) -> T | None:
    """
    Returns a validated instance of response_model, or None if no API key
    is configured (caller is expected to use its own deterministic
    fallback in that case — see intake/symptom_agent.py and
    report_parser/marker_extractor.py for examples).
    """
    settings = get_settings()
    if not settings.gemini_api_key:
        return None

    import google.generativeai as genai

    genai.configure(api_key=settings.gemini_api_key)
    model = genai.GenerativeModel(
        model_name=settings.llm_model,
        system_instruction=system_prompt,
    )

    last_error: str | None = None
    prompt = user_prompt

    for attempt in range(max_retries + 1):
        if attempt > 0:
            prompt = (
                f"{user_prompt}\n\nYour previous attempt failed validation "
                f"with error: {last_error}\nPlease correct it."
            )

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_model,
            ),
        )

        raw_text = getattr(response, "text", None)
        if not raw_text:
            last_error = "Empty response from Gemini"
            continue

        try:
            return response_model.model_validate_json(raw_text)
        except ValidationError as e:
            last_error = str(e)
            continue

    raise StructuredLLMError(
        f"Failed to get valid structured output after {max_retries + 1} attempts: {last_error}"
    )


def is_llm_available() -> bool:
    return bool(get_settings().gemini_api_key)
