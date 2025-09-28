from loguru import logger
from app.application.workflows.wf1.state import CustomState
from random import random
from app.domain.entities import BusinessEntity

def node_A(state: CustomState) -> CustomState:
    note = "We are in node A"
    return {"state_var_1": BusinessEntity(name="Noname", description=note, id="1")}

def node_A_sub1(state: CustomState) -> CustomState:
    note = "We are in node A sub 1"
    updated_note = note + state["state_var_1"].description
    return {"state_var_1": BusinessEntity(name="Noname", description=updated_note, id="1")}

def node_A_sub2(state: CustomState) -> CustomState:
    note = "We are in node A sub 2"
    updated_note = note + state["state_var_1"].description
    return {"state_var_2": updated_note}

def node_B(state: CustomState) -> CustomState:
    logger.debug(f"In node B: {state}")
    state["state_var_2"] = "We are in node B"
    return state

def node_C(state: CustomState):
    if random() > 0.5:
        return {"state_var_3": True}
    return {"state_var_3": False}

def node_D(state: CustomState):
    logger.debug(f"In node D")
    note = "We are in node D"
    return {"state_var_4": note}

def node_E(state: CustomState):
    note = "We are in node E"
    return {"state_var_5": note}
