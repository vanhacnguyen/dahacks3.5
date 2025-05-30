from flask import Blueprint, request, jsonify
from datetime import datetime
from utils.historical_rate import collect_monthly_rates

historical_bp = Blueprint('historical', __name__)

@historical_bp.route('/historical-rates', methods=['GET'])
def get_historical_rates():
    base = request.args.get('base', 'USD')
    target = request.args.get('target', 'EUR')

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
                'target': target
            })
        
        return jsonify({'success': False, 'error': 'No data avialable'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})