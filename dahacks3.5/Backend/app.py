from flask import Flask, jsonify
from routes.currency import currency_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(currency_bp)

# Add a root route for testing
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
    app.run(debug=True)