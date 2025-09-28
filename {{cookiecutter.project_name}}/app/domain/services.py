"""Domain service interfaces (dependency inversion principle)."""
from typing import Protocol

class LLMServiceInterface(Protocol):
    def generate_response(self, prompt: str) -> str: ...

