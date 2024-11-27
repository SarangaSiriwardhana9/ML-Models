from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the models
watering_model = joblib.load('watering_random_forest_model.pkl')
protection_model = joblib.load('protection_random_forest_model.pkl')

# Mapping dictionaries
location_map = {
    'PUTTALAM': 0,
    'KURUNEGALA': 1
}

watering_frequency_map = {
    0: 'No watering',
    1: 'Water once',
    2: 'Water twice'
}

protection_methods = {
    'MU': 'Mulching',
    'SH': 'Shading',
    'FW': 'Frequent Watering',
    'WB': 'Windbreaks',
    'SE': 'Soil Enrichment',
    'DS': 'Drainage System',
    'CP': 'Cover the Plants',
    'SP': 'Stake the Plants',
    'SB': 'Sand Pillows (Bags)',
    'AF': 'Avoid Over-Fertilizing',
    'PI': 'Inspect Regularly for Pests/Diseases'
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Validate location
    location = data.get('Location', '').upper()
    if location not in location_map:
        return jsonify({
            'error': 'Invalid location. Please use PUTTALAM or KURUNEGALA.'
        }), 400

    # Prepare input data
    input_data = {
        'Rainfall (mm)': data.get('Rainfall (mm)'),
        'Min Temp (°C)': data.get('Min Temp (°C)'),
        'Max Temp (°C)': data.get('Max Temp (°C)'),
        'Location': location_map[location]
    }

    df = pd.DataFrame([input_data])
    
    # Make predictions
    watering_prediction = watering_model.predict(df)[0]
    protection_prediction = protection_model.predict(df)[0]
    
    # Interpret watering prediction
    watering_frequency = watering_frequency_map[round(watering_prediction[0])]
    water_used = round(watering_prediction[1], 1)

    # Interpret protection prediction
    predicted_protection_methods = [protection_methods[method] for method in protection_prediction if method in protection_methods]

    # Prepare response
    response = {
        'location': location,
        'watering_recommendation': f"{watering_frequency} with approximately {water_used} L/m² of water.",
        'protection_methods': predicted_protection_methods
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

