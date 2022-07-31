from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DATABASE_URL = os.environ['ASYNC_DATABASE_URL']

engine = create_async_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

async def get_db():
    session = AsyncSession(engine)
    try:
        yield session
    except:
        await session.close()    
