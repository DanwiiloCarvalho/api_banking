import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.customer import Customer


class Address(Base):
    __tablename__ = "addresses"

    city: Mapped[str] = mapped_column(String(100), nullable=False)
    neighborhood: Mapped[str] = mapped_column(String(200), nullable=False)
    street: Mapped[str] = mapped_column(String(200), nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id"), unique=True, nullable=False
    )
    customer: Mapped["Customer"] = relationship(
        back_populates="address", lazy="joined"
    )
