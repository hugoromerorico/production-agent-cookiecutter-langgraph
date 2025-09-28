from typing_extensions import TypedDict
from app.domain.entities import BusinessEntity

class CustomState(TypedDict):
    state_var_1: BusinessEntity
    state_var_2: str
    state_var_3: bool
    state_var_4: list[dict]
    state_var_5: str | list[dict]
