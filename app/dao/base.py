from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete

from database import async_session_maker


class BaseDAO:
    """Класс для работы с объектами БД."""
    model = None

    @classmethod
    async def get_all_objects(cls, **kwargs):
        """Возвращает все объекты модели."""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_object(cls, **kwargs):
        """Возвращает объект модели."""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.flush()
                    new_instance_id = new_instance.id
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance_id

    @classmethod
    async def update(cls, filter_by, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount

    @classmethod
    async def delete(cls, delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError("Необходимо указать хотя бы один параметр для удаления.")

        async with async_session_maker() as session:
            async with session.begin():
                async with async_session_maker() as session:
                    async with session.begin():
                        query = select(cls.model).filter_by(**filter_by)
                        result = await session.execute(query)
                        object_to_delete = result.scalar_one_or_none()

                        if not object_to_delete:
                            return None

                        # Удаляем объект
                        await session.execute(
                            sqlalchemy_delete(cls.model).filter_by(**filter_by)
                        )

                        await session.commit()
                        return object_to_delete.id
