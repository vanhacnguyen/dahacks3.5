import os
from dotenv import load_dotenv

#Loads the key through os.getenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
HISTORICAL_KEY = os.getenv("HISTORICAL_API_KEY")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"
HISTORICAL_URL = f"https://api.freecurrencyapi.com/v1/historical/"