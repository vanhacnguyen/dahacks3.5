from flask import Blueprint, request, jsonify
from utils.exchangerate import convert_currency

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