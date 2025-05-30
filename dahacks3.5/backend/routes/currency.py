from flask import Blueprint, request, jsonify
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
    from datetime import date
    today = date.today().isoformat()

    # Sample date — change as needed
    url = f"{HISTORICAL_URL}&date={today}"
    response = request.get(url)

    if response.status_code == 200:
        data = response.json()["data"]
        currency_codes = list(data[today].keys())
        return jsonify(currency_codes)
    else:
        return jsonify([]), 500