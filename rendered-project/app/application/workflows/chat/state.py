from langgraph.graph import MessagesState
from dataclasses import dataclass
from app.domain.services import LLMServiceInterface

class ConversationState(MessagesState):
    dummy_var: str

@dataclass
class ContextSchema:
    thread_id: str
    llm_service: LLMServiceInterface
