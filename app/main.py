from typing import Union, Annotated
from fastapi import FastAPI, Query
from .currency_api.currency_api import currency_api_client

app = FastAPI()


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