from sqlalchemy import insert, update, delete, and_, text
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import func

from math import ceil
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env para o ambiente

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

db_url = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_async_engine(db_url, pool_pre_ping = True, echo = True)
Session = sessionmaker(engine, expire_on_commit = False, class_ = AsyncSession, future = True)


class Base(DeclarativeBase):
    primary_key = 'id'

    def __init__(self):
        self.columns = [column.name for column in self.__table__.columns]

    async def __aenter__(self):
            return self


    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type: raise exc_type
        return True
   
    def dict(self): return {column.name: getattr(self, column.name) for column in self.__table__.columns}


    async def create(self, **kwargs):
        data = None

        async with Session() as db:
            stmt = insert(self.__class__).values(**{column: value for column, value in kwargs.items() if column in self.columns}).returning(getattr(self.__class__, self.__class__.primary_key))
            result = await db.execute(stmt)
            await db.commit()
            inserted_id = result.scalar_one()  

            
            stmt_select = select(self.__class__).where(getattr(self.__class__, self.__class__.primary_key) == inserted_id)
            result_select = await db.execute(stmt_select)
            created_obj = result_select.scalar_one()

        return created_obj



   


    async def find_one(self, options = None, **kwargs):
        async with Session() as db:
            stmt = select(self.__class__).filter_by(**kwargs)

            if options: stmt = stmt.options(options)

            result = await db.execute(stmt)
            data = result.scalars().first()

        return data

    async def find_many(self, options = None, limit: int = None, page: int = None, last_id: int = None, **kwargs):
        async with Session() as db:
            stmt = select(self.__class__).filter_by(**kwargs)

            if options: stmt = stmt.options(options)
            if limit: stmt = stmt.limit(limit)
            if page: stmt = stmt.offset(limit * (page - 1))

            if last_id: stmt = stmt.filter(getattr(self.__class__, self.__class__.primary_key) > last_id)
            elif page: stmt = stmt.offset(limit * (page - 1))

            stmt = stmt.order_by(getattr(self.__class__, self.__class__.primary_key))

            result = await db.execute(stmt)
            data = result.scalars().all()

        return data


    async def find_or_new(self, options = None, **kwargs):
        find = await self.find_one(options, **kwargs)
        if find: return find

        return await self.create(**kwargs)