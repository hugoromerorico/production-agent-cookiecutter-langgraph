from app.application.workflows.chat.state import ConversationState
from app.domain.services import LLMServiceInterface
from app.infrastructure.llm_service import get_llm_service

def chat_node(state: ConversationState) -> dict:
    llm: LLMServiceInterface = get_llm_service()

    messages = state["messages"]
    result = llm.generate_response(messages)
    return {"messages": [result]}
