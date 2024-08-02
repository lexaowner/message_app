from app.models import Message
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

client = AsyncIOMotorClient("mongodb://mongo:27017")
db = client["message_db"]
collection = db["messages"]


async def get_messages(skip: int = 0, limit: int = 10):
    messages = []
    async for message in collection.find().skip(skip).limit(limit):
        message["_id"] = str(message["_id"])
        messages.append(message)
    return messages


async def create_message(message: Message):
    result = await collection.insert_one(message.dict())
    return str(result.inserted_id)