from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models import Message
from app.schemas import MessageCreate
from app.crud import get_messages, create_message

router = APIRouter()


@router.get("/messages/", response_model=List[Message])
async def read_messages(skip: int = 0, limit: int = 10):
    return await get_messages(skip=skip, limit=limit)


@router.post("/message/", response_model=Message)
async def create_message_endpoint(message: MessageCreate):
    message_id = await create_message(message)
    return {**message.dict(), "id": message_id}