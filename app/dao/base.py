from sqlalchemy import insert, select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:

            query = (
                insert(cls.model)
                .values(**data)
                .returning(
                    cls.model
                )
            )
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one_or_none()[cls.model.__name__]

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.mappings().all()
