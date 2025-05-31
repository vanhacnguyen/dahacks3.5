from flask import Blueprint, request, jsonify
import requests
from datetime import date
from utils.exchangerate import convert_currency
from utils.currency_utils import fetch_available_currencies
from config import BASE_URL

# Creates a blueprint for currency-related routes
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
    result = convert_currency(base, target, amount)

    # Outputs the results
    return jsonify(result)

# Fetches the available currencies from the API
@currency_bp.route('/api/currencies', methods=['GET'])
def get_currency_codes():
    currencies = fetch_available_currencies()
    if currencies:
        return jsonify(currencies)
    return jsonify({'error': 'Failed to fetch currencies'})