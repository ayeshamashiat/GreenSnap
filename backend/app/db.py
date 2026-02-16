from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client: AsyncIOMotorClient | None = None

def get_db():
    return client[settings.DB_NAME]

async def connect_db():
    global client
    client = AsyncIOMotorClient(settings.MONGODB_URI)

async def close_db():
    global client
    if client:
        client.close()
        client = None
