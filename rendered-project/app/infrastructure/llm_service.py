from app.domain.services import LLMServiceInterface

class LLMService(LLMServiceInterface):
    def __init__(self):
        pass

    def generate_response(self, messages: list[dict]) -> dict:
        """
        Generate a response from the LLM.
        """
        if not messages:
            return {"role": "assistant", "content": ""}
        return {"role": "assistant", "content": messages[-1]["content"]}
