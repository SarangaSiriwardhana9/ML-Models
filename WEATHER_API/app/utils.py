import pandas as pd
from app.weather_data.protection_methods import protection_methods, get_protection_explanation
from app.weather_data.weather_conditions import assess_weather_condition

location_map = {
    'PUTTALAM': 0,
    'KURUNEGALA': 1
}

watering_frequency_map = {
    0: 'No watering',
    1: 'Water once',
    2: 'Water twice'
}

fertilizer_recommendation_map = {
    0: 'Not Recommended',
    1: 'Recommended'
}

def prepare_input_data(data, model_type):
    location = data.get('Location', '').upper()
    if location not in location_map:
        raise ValueError('Invalid location. Please use PUTTALAM or KURUNEGALA.')

    if model_type == 'fertilizer':
        input_data = {
            'Rainfall (mm)': data.get('Rainfall (mm)'),
            'Location': location_map[location]
        }
    else:
        input_data = {
            'Rainfall (mm)': data.get('Rainfall (mm)'),
            'Min Temp (°C)': data.get('Min Temp (°C)'),
            'Max Temp (°C)': data.get('Max Temp (°C)'),
            'Location': location_map[location]
        }
    return pd.DataFrame([input_data])

def interpret_watering(prediction):
    watering_frequency = watering_frequency_map[round(prediction[0])]
    water_used = round(prediction[1], 1)
    return f"{watering_frequency} with approximately {water_used} L/m² of water."

def interpret_protection(prediction, weather_data):
    weather_condition = assess_weather_condition(weather_data)
    recommended_methods = [protection_methods[method] for method in prediction if method in protection_methods]
    
    detailed_recommendations = []
    for method in recommended_methods:
        explanation = get_protection_explanation(method, weather_condition)
        detailed_recommendations.append({
            "method": method,
            "explanation": explanation
        })
    
    return {
        "weather_condition": weather_condition,
        "recommendations": detailed_recommendations
    }

def interpret_fertilizer(prediction):
    return fertilizer_recommendation_map[prediction]

