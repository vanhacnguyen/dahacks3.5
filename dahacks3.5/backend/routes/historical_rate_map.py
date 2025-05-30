from flask import Blueprint, request, jsonify
from datetime import datetime
from utils.historical_rate import collect_monthly_rates
import requests
from config import BASE_URL

historical_bp = Blueprint('historical', __name__)

def get_available_currencies():
    """Helper function to fetch available currencies"""
    url = f"{BASE_URL}/codes"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [code[0] for code in data.get("supported_codes", [])]
    except Exception:
        return []

@historical_bp.route('/historical-rates', methods=['GET'])
def get_historical_rates():
    # Get available currencies
    available_currencies = get_available_currencies()
    
    # Get parameters with defaults
    base = request.args.get('base', 'USD').upper()
    target = request.args.get('target', 'EUR').upper()
    
    # Validate currencies
    if not available_currencies:
        return jsonify({'success': False, 'error': 'Unable to fetch currency list'})
    
    if base not in available_currencies:
        return jsonify({'success': False, 'error': f'Invalid base currency: {base}'})
    if target not in available_currencies:
        return jsonify({'success': False, 'error': f'Invalid target currency: {target}'})

    # Get date parameters
    current_date = datetime.now()
    year = int(request.args.get('year', current_date.year))
    month = int(request.args.get('month', current_date.month))

    try:
        dates, rates = collect_monthly_rates(base, target, year, month)

        if dates and rates:
            return jsonify({
                'success': True,
                'dates': dates,
                'rates': rates,
                'base': base,
                'target': target,
                'available_currencies': available_currencies
            })
        
        return jsonify({'success': False, 'error': 'No data available'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})