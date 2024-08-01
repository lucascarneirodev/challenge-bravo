from sqlmodel import Field, SQLModel, create_engine
from typing import List

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
  id: int | None = Field(default=None, primary_key=True)
  symbol: str
  symbol_native: str
  decimal_digits: int
  rounding: int
  code: str = Field(default=None, primary_key=True)
  name: str
  name_plural: str
  type: str
  countries: List[str]

## Example of response for a GET exchange from currencyapi
# "AED": {
#             "code": "AED",
#             "value": 3.67306

### base_currency_code --> foreign_currency_code
### eg: how much is X "base_currency_code"/USD in "foreign_currency_code"/BRL

### monetary data in postgresql:
### NUMERIC(precision, scale)
### We use the following terms below: The precision of a numeric is the total count of significant digits in the whole number, that is, the number of digits to both sides of the decimal point. The scale of a numeric is the count of decimal digits in the fractional part, to the right of the decimal point. So the number 23.5141 has a precision of 6 and a scale of 4. Integers can be considered to have a scale of zero.
### NUMERIC(22,5)
### allows for 999 trillions and 5 fractional parts to the right of the decimal point PLUS an extra digit for future-proofing just in case (1 quadrillion)


class CurrencyExchange(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  base_currency_code: str #foreign key
  foreign_currency_code: str #foreign key
  value: float #TODO: change to NUMERIC(22,5)
  date: str #Date when the rate was calculated, could be automatic based on when added to db


#### user tables

class users(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  email: str
  password: str
  created_on: str

class api_keys(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  user_id: int #foreign key
  api_key: str
  created_on: str
  permissions: str # Read + Write, Read
  status: str # Valid, Deprecated
  monthly_quota: int
  quota_usage: int
  quota_left: int


