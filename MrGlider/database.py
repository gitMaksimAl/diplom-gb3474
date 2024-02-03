from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os

from models import EventBase


SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=True,
    conect_args={"check_same_thread": False}
)
async_session = sessionmaker(autocommit=False, bind=engine, class_=AsyncSession)


async def startup():
    async with engine.begin() as connection:
        await connection.run_sync(EventBase.metadata.create_all())


async def shutdown():
    await engine.dispose()
