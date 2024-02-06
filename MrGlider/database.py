from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from config import DATABASE_URI

from models import Base


engine = create_async_engine(
    DATABASE_URI,
    echo=True,
    conect_args={"check_same_thread": False}
)
async_session = sessionmaker(autocommit=False, bind=engine, class_=AsyncSession)


async def startup():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all())


async def shutdown():
    await engine.dispose()
