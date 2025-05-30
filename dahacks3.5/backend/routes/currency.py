from flask import Blueprint, request, jsonify
import requests
from datetime import date
from utils.exchangerate import convert_currency
from config import HISTORICAL_URL, HISTORICAL_KEY, BASE_URL

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