from langgraph.checkpoint.memory import InMemorySaver
from app.application.workflows.chat.graph import get_graph
from langgraph.types import StateSnapshot
from app.application.workflows.chat.state import ContextSchema
from app.infrastructure.llm_service import LLMService


class Chat:
    def __init__(self):
        self.llm_service = LLMService()
        self.checkpointer = InMemorySaver()
        self.graph = get_graph(self.checkpointer)
        self.context = ContextSchema(llm_service=self.llm_service)


    def execute(self,user_message: str, user_id: str):
        result = self.graph.invoke(
                    {"messages": [{"role": "user", "content": user_message}]},
                    {"configurable": {"thread_id": user_id}, "context": self.context},
                )
        return result
    
    def get_state(self, user_id: str):
        config = {"configurable": {"thread_id": user_id}}
        snapshot: StateSnapshot = self.graph.get_state(config)
        return snapshot

