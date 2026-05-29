from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base


class BaseRepository[ModelType: Base]:
    def __init__(self, session: AsyncSession, model: type[ModelType]) -> None:
        self.session = session
        self.model = model

    async def create(self, entity: ModelType) -> ModelType:
        self.session.add(entity)
        await self.session.flush()
        return entity

    async def get_by_id(self, entity_id: UUID) -> ModelType | None:
        return await self.session.get(self.model, entity_id)

    async def list_all(self, limit: int = 100, skip: int = 0) -> list[ModelType]:
        stmt = select(self.model).limit(limit).offset(skip)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def update(self, entity: ModelType) -> ModelType:
        await self.session.flush()
        return entity

    async def delete(self, entity: ModelType) -> None:
        await self.session.delete(entity)
        await self.session.flush()
