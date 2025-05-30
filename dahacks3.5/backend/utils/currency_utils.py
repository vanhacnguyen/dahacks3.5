import requests
from config import BASE_URL

def fetch_available_currencies():

    url = f"{BASE_URL}/codes"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("result") == "success":
                return [code[0] for code in data.get("supported_codes", [])]
    except Exception:
        pass
    return []

'''
url = f"{BASE_URL}/codes"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("result") == "success":
                codes = [code[0] for code in data.get("supported_codes", [])]
                return jsonify(codes)
            else:
                return jsonify({'error': 'API returned error'}), 500
        else:
            return jsonify({'error': f'status {response.status_code}'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''