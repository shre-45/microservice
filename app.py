from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Simulate a weather endpoint
@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Unknown')
    # This is mocked data; in real apps you call an external API
    weather_data = {
        "city": city,
        "temperature": "31°C",
        "status": "Sunny",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return jsonify(weather_data)

# Health check
@app.route('/')
def home():
    return "Weather Microservice is up and running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
