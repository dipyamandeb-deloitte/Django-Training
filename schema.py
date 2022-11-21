from pydantic import BaseModel

class Hashers(BaseModel):
    id:int
    name:str
    email:str
class Description(BaseModel):
    id:int
    title:str
    description:str