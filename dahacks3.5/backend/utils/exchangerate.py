import requests
from config import API_KEY, BASE_URL # Imports API credentials from the config file

def convert_currency(base, target, amount):

    # Construct API endpoint URL with parameters
    url = f"{BASE_URL}/pair/{base}/{target}/{amount}"
    res = requests.get(url) # Makes a GET request to the api

    # Checks if the request was successful (Which is status code 200)
    if res.status_code == 200:
        data = res.json() # Returns the results
        return {
            'base': base,
            'target': target,
            'rate': data.get('conversion_rate'),
            'converted_amount': data.get('conversion_result')  # This is what frontend expects
        }
    else: # Incase it's not successful returns a error message
        return {'error': 'Failed to fetch the conversion data.'}
    

if __name__ == "__main__":
    # Test the conversion function
    result = convert_currency("USD", "EUR", 100)
    print(result)