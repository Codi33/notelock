import motor.motor_asyncio
from odmantic import AIOEngine

from .settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
engine = AIOEngine(client, database="notelock")
