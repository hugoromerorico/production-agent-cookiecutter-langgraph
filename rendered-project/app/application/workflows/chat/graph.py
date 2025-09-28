
from functools import lru_cache
from loguru import logger

from langgraph.graph import END, START, StateGraph
from app.application.workflows.chat.state import ConversationState, ContextSchema
from langgraph.checkpoint.memory import InMemorySaver
from app.application.workflows.chat.nodes import chat_node

@lru_cache(maxsize=1)
def create_workflow_graph():
    """Creates a single-node graph with the agent."""
    graph_builder = StateGraph(ConversationState, context_schema=ContextSchema)
    
    graph_builder.add_node("chat_node", chat_node)
    graph_builder.add_edge(START, "chat_node")
    graph_builder.add_edge("chat_node", END)
    
    return graph_builder


def get_graph(checkpointer: InMemorySaver | None = None):
    """Returns the compiled graph."""
    logger.debug(f"Creating graph with state: {ConversationState}")
    if checkpointer:
        return create_workflow_graph().compile(checkpointer=checkpointer)
    return create_workflow_graph().compile()



graph = get_graph() # For development purposes