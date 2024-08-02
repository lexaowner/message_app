from pydantic import BaseModel, Field
from typing import Optional


class Message(BaseModel):
    id: Optional[str] = Field(None, alias='id')
    author: str
    text: str


class MessageCreate(BaseModel):
    author: str
    text: str