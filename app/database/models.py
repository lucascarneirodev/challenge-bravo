from sqlmodel import Field, SQLModel, create_engine
from typing import List
from decimal import Decimal
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DECIMAL, UniqueConstraint
from sqlalchemy.dialects.mysql import VARCHAR
from datetime import datetime, timedelta

class Currency(SQLModel, table=True):
  id: int | None = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
  symbol: str = Field(max_length=255)
  symbol_native: str = Field(max_length=255)
  decimal_digits: int
  rounding: int
  code: str = Field(sa_column=Column(String(255), unique=True, nullable=False))
  name: str = Field(max_length=255)
  name_plural: str = Field(max_length=255)
  currency_type: str = Field(max_length=255)
  countries: List[str] = Field(sa_column=Column(JSON))

  __table_args__ = (UniqueConstraint('code', name='uq_currency_code'),)


class CurrencyExchange(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  currency_code: str = Field(sa_column=Column(String(255), ForeignKey("currency.code")))
  value: Decimal = Field(sa_column=Column(DECIMAL(21, 5), nullable=False))
  date: datetime = Field(default_factory=datetime.utcnow)


