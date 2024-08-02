from pydantic import BaseModel

class MessageCreate(BaseModel):
    author: str
    text: str