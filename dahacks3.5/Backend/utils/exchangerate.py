import requests
from config import API_KEY, BASE_URL # Imports API credentials from the config file

def convert_currency(base, target, amount):

    # Construct API endpoint URL with parameters
    url = f"{BASE_URL}/pair/{base}/{target}/{amount}"
    res = requests.get(url) # Makes a GET request to the api

    # Checks if the request was successful (Which is status code 200)
    if res.status_code == 200:
        return res.json() # Returns the results
    else: # Incase it's not successful returns a error message
        return {'error': 'Failed to fetch the conversion data.'}