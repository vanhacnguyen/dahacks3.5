import requests
from config import BASE_URL

def fetch_available_currencies():

    # Construct API endpoint URL with parameters
    url = f"{BASE_URL}/codes"

    try:
        # Makes a GET request to the API
        response = requests.get(url)

        # Checks if request was successful
        if response.status_code == 200:
            data = response.json()

            # Verifys if the API return was successfull or not
            if data.get("result") == "success":
                
                # Extracts the currency node from supported_codes array
                # Each code is the first element of the sub-array
                return [code[0] for code in data.get("supported_codes", [])]
    except Exception:

        # if any errors occur, ignore the request and return a empty list
        pass

    # returns a empty list if anything fails
    return []