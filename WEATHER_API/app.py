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
    0: 'ජලය දැමීම අත්‍යවශ්‍ය නොවේ',
    1: 'ආසන්න වශයෙන් {water_used} L/m² බැගින් ජලය එක් වරක් ‍යොදන්න',
    2: 'ආසන්න වශයෙන් {water_used} L/m² බැගින් ජලය දෙවරක් ‍යොදන්න'
}

protection_methods = {
    'MU': 'මල්චින්ග් (Mulching)',
    'SH': 'සෙඩ් නිවරණ (Shading)',
    'FW': 'පෙරළි ජලය යොදීම (Frequent Watering)',
    'WB': 'සුලඟ ආරක්ෂක (Windbreaks)',
    'SE': 'බිම පෝෂණය (Soil Enrichment)',
    'DS': 'දිය අයදුම් ක්‍රම (Drainage System)',
    'CP': 'ගස් ආවරණය කිරීම (Cover the Plants)',
    'SP': 'ගස් ස්ථිර කිරීම (Stake the Plants)',
    'SB': 'පොලව ආරක්ෂාව සඳහා වැලි බෑග් (Sand Pillows)',
    'AF': 'ඉහළ පොහොර යෙදීම වැලැක්වීම (Avoid Over-Fertilizing)',
    'PI': 'පළිබෝධ පරීක්ෂාව (Inspect for Pests/Diseases)'
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
    watering_frequency = int(round(watering_prediction[0]))
    water_used = round(watering_prediction[1], 1)
    watering_recommendation = watering_frequency_map[watering_frequency].format(water_used=water_used)

    # Interpret protection prediction
    predicted_protection_methods = [protection_methods[method] for method in protection_prediction if method in protection_methods]

    # Prepare response
    response = {
        'location': location,
        'watering_recommendation': watering_recommendation,
        'protection_methods': predicted_protection_methods
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
