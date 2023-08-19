from pydantic import BaseModel
from typing import Optional
from uuid import UUID,uuid4


class person(BaseModel):
    id: Optional[int]
    name: str
    family: str

class users(BaseModel):
    id:Optional[UUID]=uuid4
    user_name:str
    password:str