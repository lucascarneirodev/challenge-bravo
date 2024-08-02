import os
from dotenv import load_dotenv, find_dotenv
import currencyapicom

load_dotenv(find_dotenv(raise_error_if_not_found=False))

currency_api_client = currencyapicom.Client(os.environ["CURRENCY_API_KEY2"])

