from app.domain.services import LLMServiceInterface
from functools import lru_cache
from loguru import logger
from langchain_core.messages import AnyMessage, AIMessage

class LLMService(LLMServiceInterface):
    def __init__(self):
        pass

    def generate_response(self, messages: list[AnyMessage]) -> AIMessage:
        """
        Generate a response from the LLM.
        """
        logger.debug(f"Messages: {messages}")
        if not messages:
            return AIMessage(content="")
        return AIMessage(content=messages[-1].text()[::-1])

@lru_cache(maxsize=1)
def get_llm_service():
    return LLMService()
