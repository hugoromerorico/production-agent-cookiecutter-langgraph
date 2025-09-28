
from functools import lru_cache
from loguru import logger
from langgraph.graph import END, START, StateGraph
from app.application.workflows.wf1.state import CustomState
from app.application.workflows.wf1.nodes import (
    node_A,
    node_B,
    node_C,
    node_D,
    node_E,
    node_A_sub1,
    node_A_sub2,
)

@lru_cache(maxsize=1)
def create_workflow_graph() -> StateGraph:
    graph_builder = StateGraph(CustomState)
    
    #region nodes
    graph_builder.add_node("nodeA", node_A)
    graph_builder.add_node("nodeA_sub1", node_A_sub1)
    graph_builder.add_node("nodeA_sub2", node_A_sub2)
    graph_builder.add_node("nodeB", node_B)
    graph_builder.add_node("nodeC", node_C)
    graph_builder.add_node("nodeD", node_D)
    graph_builder.add_node("nodeE", node_E)
    
    #region edges
    graph_builder.add_edge(START, "nodeA")
    graph_builder.add_edge("nodeA", "nodeA_sub1")
    graph_builder.add_edge("nodeA", "nodeA_sub2")
    graph_builder.add_edge("nodeA_sub1", "nodeB")
    graph_builder.add_edge("nodeA_sub2", "nodeB")
    graph_builder.add_edge("nodeB", "nodeC")
    graph_builder.add_conditional_edges("nodeC", lambda state: state.get("state_var_3", False), {
        True: "nodeD",
        False: "nodeE"
    })
    graph_builder.add_edge("nodeD", END)
    graph_builder.add_edge("nodeE", END)

    return graph_builder


def get_graph():
    return create_workflow_graph().compile()

graph = get_graph() # For development purposes

