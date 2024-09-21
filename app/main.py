from typing import Union, Annotated
from fastapi import FastAPI, Query, HTTPException
from currency_api.currency_api import currency_api_client
from database.models import Currency, CurrencyExchange
from database import db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()
    db.load_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint converting a currency to another
@app.get("/convert/")
async def currency_converter(currency_from: Annotated[str | None, Query(alias="from")] = None, currency_to: Annotated[str | None, Query(alias="to")] = None, amount: float = 1.00):
    return {
        "from": f'{currency_from}',
        "to": f'{currency_to}',
        "amount": f'{amount}'
    }

@app.get("/test")
async def test_currency_api():
    return currency_api_client.status()


@app.get("/currencies/", response_model=list[Currency])
def get_currencies():
    results = db.read_all_currencies()
    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="No Currencies found!")
    
@app.post("/currency/add", response_model=Currency)
async def add_currency(currency: Currency):
    result = db.create_currency(currency)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Currency already exists!")
    


@app.get("/currency/find/{currency_code}", response_model=Currency)
def get_currency(currency_code: str):
    result = db.read_currency(currency_code)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Currency not found")

@app.get("/exchange/", response_model=list[CurrencyExchange])
def get_exchanges():
    results = db.read_all_currency_exchanges()
    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="No Exchanges found!")
    
@app.get("/exchange/find/{currency_code}", response_model=CurrencyExchange)
def get_exchange(currency_code: str):
    result = db.read_currency_exchange(currency_code)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Exchange not found")

@app.post("/exchange/add", response_model=CurrencyExchange)
def add_exchange(currency_exchange: CurrencyExchange):
    result = db.create_currency_exchange(currency_exchange)
    if result:
        return result
    else:
        raise HTTPException(status_code=503, detail="Service momentarily unavailable. Try again later.")