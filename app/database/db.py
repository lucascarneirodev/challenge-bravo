import os
from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy import URL
from sqlalchemy.exc import NoResultFound
from dotenv import load_dotenv, find_dotenv
from .models import Currency, CurrencyExchange

load_dotenv(find_dotenv(raise_error_if_not_found=False))

# Create database connection URL for Database Engine (SQLAlchemy)
url_object = URL.create(
    "mariadb+mariadbconnector",
    username=os.environ["MARIADB_USER"],
    password=os.environ["MARIADB_PASSWORD"],  # plain (unescaped) text
    host="db",
    database=os.environ["MARIADB_DATABASE"],
)

engine = create_engine(url_object, echo=True)

# CREATE DB AND TABLES
def create_db_and_tables():
    '''
    Creates the database and tables using the engine created on the database.db module.
    '''
    SQLModel.metadata.create_all(engine)


#CRUD Endpoints

# Create
#TODO
def create_currency_exchange(currency_exchange: CurrencyExchange) -> CurrencyExchange | None:
    '''
    Creates a currency_exchange rate in the database.
    A currency_exchange rate already exists if the currency_exchange object matches an existing currency_exchange in base_currency_code, foreign_currency_code and creation date (down to the second).

    If a new currency_exchange is created with the same base_currency_code, foreign_currency_code and similar creation date (eg. a difference of seconds), it will be considered a new currency exchange rate.

    A currency_exchange rate can be updated by using the update_currency_exchange function.

    Args:
    currency_exchange (CurrencyExchange): The currency exchange rate to be created.

    Returns:
    CurrencyExchange: The created currency exchange rate. If the currency exchange rate already exists, returns None.

    '''
    pass

#TODO
def create_currency(currency: Currency) -> Currency | None:
    '''
    Creates a currency in the database.

    Args:
    currency (Currency): The currency to be created.

    Returns:
    Currency: The created currency. If the currency already exists, returns None.
    '''
    pass

# Read
#TODO
def read_currency(currency_symbol: str) -> Currency | None:
    '''
    Search and return a currency from the database defined by the currency symbol.

    Args:
    currency_symbol (str): The currency symbol of the currency to be searched. Example: 'BRL'

    Returns:
    Currency: The currency found. If the currency does not exist, returns None.
    '''
    pass

#TODO
def read_all_currencies() -> list[Currency] | None:
    '''
    Search and return all currencies in the database.

    Returns:
    A list of currencies in the database. If no currency is found, returns None.
    '''
    pass

#TODO
def read_currency_exchange(base_currency_code: str, foreign_currency_code: str) -> CurrencyExchange | None:
    '''
    Search and return the latest currency exchange rates from the database.
    A CurrencyExchange object is defined by the combination of the currency codes (base_currency_code + foreign_currency_code).
    If no combination of currency codes is given, returns the latest currency exchange rate for every currency code ever.

    Args:
    base_currency_code (str): The currency code for the base currency from which the exchange rate is calculated. Example: 'BRL'

    foreign_currency_code (str): The currency code for the foreign currency to which the exchange rate is calculated. Example: 'USD'

    Returns:
    CurrencyExchange: The latest CurrencyExchange object. If no data is found, returns None.
    '''

    pass

#TODO
def read_all_currency_exchanges(base_currency_code: str, foreign_currency_code: str) -> list[CurrencyExchange] | None:
    '''
    Search and return all historical data for currency exchange rates from the database.
    A CurrencyExchange object is defined by the combination of the currency codes (base_currency_code + foreign_currency_code).
    If no combination of currency codes is given, returns every currency exchange rate for every currency code ever.

    Args:
    base_currency_code (str): The currency code for the base currency from which the exchange rate is calculated. Example: 'BRL'

    foreign_currency_code (str): The currency code for the foreign currency to which the exchange rate is calculated. Example: 'USD'

    Returns:
    list[CurrencyExchange]: A list of CurrencyExchange objects. If no historical data is found, returns None.

    '''
    pass

# Update
#TODO
def update_currency(currency: Currency) -> Currency | None:
    '''
    Updates a currency in the database.

    Args:
    currency (Currency): The currency to be updated.

    Returns:
    Currency: The updated currency. If the currency does not exist, returns None.
    '''
    pass

#TODO
def update_currency_exchange(currency_exchange: CurrencyExchange) -> CurrencyExchange | None:
    '''
    Updates a currency exchange rate in the database by the ID. If the currency exchange rate does not exist, it will not be created.

    A currency_exchange can only be updated for the value. If you want to update the base_currency_code, foreign_currency_code or date, you must create a new currency_exchange and delete the old one (or leave it be for historical purpose).

    Args:
    currency_exchange (CurrencyExchange): The currency exchange rate to be updated.

    Returns:
    CurrencyExchange: The updated currency exchange rate. If the currency exchange rate does not exist, returns None.
    '''
    pass

# Delete
#TODO
def delete_currency(currency_symbol: str) -> Currency | None:
    '''
    Deletes a currency from the database defined by the currency symbol.
    Deleting a currency will also delete all currency exchange rates that have the currency symbol as the base currency or foreign currency.

    Args:
    currency_symbol (str): The currency symbol of the currency to be deleted. Example: 'BRL'

    Returns:
    Currency: The currency that was deleted. If the currency does not exist, returns None.
    '''
    pass

#TODO
def delete_currency_exchange(base_currency_code: str, foreign_currency_code: str) -> CurrencyExchange | None:
    '''
    Deletes the latest currency exchange rate from the database defined by a combination of the currency codes (base_currency_code + foreign_currency_code).

    If you want to delete a historical currency exchange rate from the database, you must use the delete_currency_exchange_by_id function.

    Args:
    base_currency_code (str):
    foreign_currency_code (str):

    Returns:
    CurrencyExchange: The currency exchange rate that was deleted. If the currency exchange rate does not exist, returns None.
    '''
    pass

#TODO
def delete_currency_exchange_by_id(currency_exchange_id: str) -> CurrencyExchange | None:
    '''
    Deletes a currency exchange rate from the database defined by the id.

    Args:
    currency_exchange_id (uuid):

    Returns:
    CurrencyExchange: The currency exchange rate that was deleted. If the currency exchange rate does not exist, returns None.
    '''
    pass