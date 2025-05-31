import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get API keys from the .env file
API_KEY = os.getenv("EXCHANGE_API_KEY")
HISTORICAL_KEY = os.getenv("HISTORICAL_API_KEY")

# Constructs base URLS for API endpoints
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"
HISTORICAL_URL = f"https://api.freecurrencyapi.com/v1/historical/"