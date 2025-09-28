from pydantic import BaseModel

class BusinessEntity(BaseModel):
    name: str
    description: str
    id: str
