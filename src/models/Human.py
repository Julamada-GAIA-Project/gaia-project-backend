from pydantic import BaseModel

class Human(BaseModel):
    name: str
    lastName: str
    physical: int
    studies: str