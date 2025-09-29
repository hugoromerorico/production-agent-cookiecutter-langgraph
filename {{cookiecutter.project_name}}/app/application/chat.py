from langgraph.checkpoint.memory import InMemorySaver
from app.application.workflows.chat.graph import get_graph
from langgraph.types import StateSnapshot
from app.infrastructure.llm_service import LLMService


class Chat:
    def __init__(self):
        self.checkpointer = InMemorySaver()
        self.graph = get_graph(self.checkpointer)


    def execute(self,user_message: str, thread_id: str):
        result = self.graph.invoke(
                    {"messages": [{"role": "user", "content": user_message}]},
                    {"configurable": {"thread_id": thread_id}},
                )
        return result
    
    def get_state(self, thread_id: str):
        config = {"configurable": {"thread_id": thread_id}}
        snapshot: StateSnapshot = self.graph.get_state(config)
        return snapshot
