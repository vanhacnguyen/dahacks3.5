import requests
from config import HISTORICAL_KEY, HISTORICAL_URL
from datetime import datetime
from calendar import monthrange
import matplotlib.pyplot as plt

def get_daily_rate(base_currency, target_currency, year, month, day):
    date_str = f"{year}-{month:02}-{day:02}"
    params = {
        "apikey": HISTORICAL_KEY,
        "date": date_str,
        "base_currency": base_currency,
        "currencies": target_currency
    }
    response = requests.get(HISTORICAL_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["data"].get(date_str, {}).get(target_currency)
    else:
        print(f"Failed on {date_str}:", response.status_code)
        return None

def collect_monthly_rates(base_currency, target_currency, year, month):
    days_in_month = monthrange(year, month)[1]
    dates = []
    rates = []

    for day in range(1, days_in_month + 1):
        rate = get_daily_rate(base_currency, target_currency, year, month, day)
        print(f"Rate for {base_currency}->{target_currency} on {year}-{month:02}-{day:02}: {rate}")
        if rate is not None:
            dates.append(f"{month:02}/{day:02}")
            rates.append(rate)
    
    return dates, rates
