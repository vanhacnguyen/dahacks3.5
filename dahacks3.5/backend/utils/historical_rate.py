import requests
from config import HISTORICAL_KEY, HISTORICAL_URL
from datetime import datetime
from calendar import monthrange
import matplotlib.pyplot as plt

def get_daily_rate(base_currency, target_currency, year, month, day):

    # Formats the date string for API request (YYYY-MM-DD)
    date_str = f"{year}-{month:02}-{day:02}"

    # Setups the API request parameters
    params = {
        "apikey": HISTORICAL_KEY,
        "date": date_str,
        "base_currency": base_currency,
        "currencies": target_currency
    }

    # Make a API request for the historical rate
    response = requests.get(HISTORICAL_URL, params=params)

    # Checks if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data["data"].get(date_str, {}).get(target_currency)
    else:
        print(f"Failed on {date_str}:", response.status_code)
        return None

def collect_monthly_rates(base_currency, target_currency, year, month):

    # Gets the number of days in the specified month
    days_in_month = monthrange(year, month)[1]
    dates = []
    rates = []

    # Collects the reates for every 3 days
    for day in range(1, days_in_month + 1, 3):
        rate = get_daily_rate(base_currency, target_currency, year, month, day)
        if rate:
            dates.append(f"{month:02}/{day:02}")
            rates.append(rate)
    
    return dates, rates

def plot_rates(dates, rates, base_currency, target_currency, year, month):

    # Creates figures with a specified size
    plt.figure(figsize=(10, 5))
    
    # Plot the rates with markers and lines
    plt.plot(dates, rates, marker='o', linestyle='-', color='blue')

    # Add some titles and labels
    plt.title(f"Exchange Rate: {base_currency} → {target_currency} ({year}-{month:02})")
    plt.xlabel("Date")
    plt.ylabel(f"Rate to {target_currency}")

    # Customizes the plot
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Test code to make sure it runs well
if __name__ == "__main__":
    base = "USD"
    target = "EUR"
    year = 2024
    month = 5

    try:
        dates, rates = collect_monthly_rates(base, target, year, month)

        if dates and rates:
            print(f"Collected {len(dates)} data points")
            print("Dates:", dates)
            print("Rates:", rates)

            plot_rates(dates, rates, base, target, year, month)
        else:
            print("No data collected")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")