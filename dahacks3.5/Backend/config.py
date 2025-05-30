import os
from dotenv import load_dotenv

#Loads the key through os.getenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "Placeholder Url"