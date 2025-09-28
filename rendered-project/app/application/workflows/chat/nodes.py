from app.application.workflows.chat.state import ContextSchema
from langgraph.runtime import Runtime
from app.application.workflows.chat.state import ConversationState
from app.domain.services import LLMServiceInterface

def chat_node(state: ConversationState, runtime: Runtime[ContextSchema]) -> dict:
    llm: LLMServiceInterface = runtime.context.llm_service

    messages = state["messages"]
    result = llm.generate_response(messages)
    return {"messages": [result]}
