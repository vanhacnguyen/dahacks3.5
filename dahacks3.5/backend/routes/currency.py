from flask import Blueprint, request, jsonify
import requests
from datetime import date
from utils.exchangerate import convert_currency
from config import HISTORICAL_URL

currency_bp = Blueprint('currency', __name__)

@currency_bp.route('/convert', methods=['GET'])
def convert():

    # Gets the parameters for the request URL
    base = request.args.get('base')
    target = request.args.get('target')
    amount = request.args.get('amount')

    # Validates the input
    if not base or not target or amount is None:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    # Calls the function that fetches exchange rate data
    result =convert_currency(base, target, amount)

    # Outputs the results
    return jsonify(result)

@currency_bp.route('/api/currencies', methods=['GET'])
def get_currency_codes():
    today = date.today().isoformat()
    url = f"{HISTORICAL_URL}&date={today}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("data", {})
            # Safely get the nested date dictionary
            day_data = data.get(today, {})
            currency_codes = list(day_data.keys())
            return jsonify(currency_codes)
        else:
            return jsonify({'error': f'Status {response.status_code}'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500