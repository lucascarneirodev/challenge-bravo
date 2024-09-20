from sqlmodel import Field, SQLModel, create_engine
from typing import List
from decimal import Decimal
from sqlalchemy import Column, Integer, String, ForeignKey, JSON,DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR

## example of a currency info from currencyapi
# "AED": {
#     "symbol": "AED",
#     "name": "United Arab Emirates Dirham",
#     "symbol_native": "د.إ",
#     "decimal_digits": 2,
#     "rounding": 0,
#     "code": "AED",
#     "name_plural": "UAE dirhams",
#     "type": "fiat",
#     "countries": [
#         "AE"
#     ]
# },

class Currency(SQLModel, table=True):
  id: int | None = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
  symbol: str = Field(max_length=255, primary_key=True)
  symbol_native: str = Field(max_length=255)
  decimal_digits: int
  rounding: int
  code: str = Field(max_length=255, primary_key=True)
  name: str = Field(max_length=255)
  name_plural: str = Field(max_length=255)
  currency_type: str = Field(max_length=255)
  countries: List[str] = Field(sa_column=Column(JSON))

## Example of response for a GET exchange from currencyapi
# "AED": {
#             "code": "AED",
#             "value": 3.67306

### base_currency_code --> foreign_currency_code
### eg: how much is X "base_currency_code"/USD in "foreign_currency_code"/BRL

### monetary data in postgresql:
### NUMERIC(precision, scale)
### We use the following terms below: The precision of a numeric is the total count of significant digits in the whole number, that is, the number of digits to both sides of the decimal point. The scale of a numeric is the count of decimal digits in the fractional part, to the right of the decimal point. So the number 23.5141 has a precision of 6 and a scale of 4. Integers can be considered to have a scale of zero.
### NUMERIC(21,5) ===> Decimal = Field(default=0, max_digits=21, decimal_places=5)
## 9.999.999.999.999.999,99999
### allows for 999 trillions and 5 fractional parts to the right of the decimal point PLUS an extra digit for future-proofing just in case (1 quadrillion)

# Decimal = Field(default=0, max_digits=5, decimal_places=3)


class CurrencyExchange(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  base_currency_code: str = Field(sa_column=Column(String(255), ForeignKey("currency.code")))
  foreign_currency_code: str = Field(sa_column=Column(String(255), ForeignKey("currency.code")))
  value: Decimal = Field(sa_column=Column(DECIMAL(21, 5), nullable=False))
  date: str = Field(max_length=255) #Date when the rate was calculated, could be automatic based on when added to db


#### user tables

# class users(SQLModel, table=True):
#   id: int | None = Field(default=None, primary_key=True)
#   email: str
#   password: str
#   created_on: str

# class api_keys(SQLModel, table=True):
#   id: int | None = Field(default=None, primary_key=True)
#   user_id: int #foreign key
#   api_key: str
#   created_on: str
#   permissions: str # Read + Write, Read
#   status: str # Valid, Deprecated
#   monthly_quota: int
#   quota_usage: int
#   quota_left: int


