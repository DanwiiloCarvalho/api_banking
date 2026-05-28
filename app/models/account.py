from decimal import Decimal
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.customer import Customer
    from app.models.transaction import Transaction


class Account(Base):
    __tablename__ = "accounts"

    balance: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    bank_branch: Mapped[str] = mapped_column(String(100), nullable=False)
    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id"), nullable=False
    )
    customer: Mapped["Customer"] = relationship(
        back_populates="accounts", lazy="joined"
    )
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="account", cascade="all, delete-orphan", lazy="raise"
    )
