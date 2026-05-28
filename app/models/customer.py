from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import CHAR, Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.account import Account
    from app.models.address import Address


class Customer(Base):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    accounts: Mapped[list["Account"]] = relationship(
        back_populates="customer", lazy="raise", cascade="all, delete-orphan")
    address: Mapped["Address | None"] = relationship(
        back_populates="customer",
        lazy="raise",
        uselist=False,
        cascade="all, delete-orphan",
    )
