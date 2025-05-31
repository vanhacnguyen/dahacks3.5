from flask import Flask, jsonify
from routes.currency import currency_bp
from routes.historical_rate_map import historical_bp
from flask_cors import CORS

# Initialize Flask Application
app = Flask(__name__)
CORS(currency_bp) # Enables CORS for all routes

# Register the blueprint
app.register_blueprint(currency_bp) # Handles currency conversion
app.register_blueprint(historical_bp) # handles the historical rate data

# Root route tat documents available API endpoints
@app.route('/')
def home():
    return jsonify({
        "message": "Currency Exchange API",
        "endpoints": {
            "convert": "/convert?base=USD&target=EUR&amount=100",
            "currencies": "/api/currencies"
        }
    })

if __name__ == '__main__':
    app.run(debug=True) # Runs it in debug mode for testing