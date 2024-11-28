import pandas as pd
from datetime import datetime
from app.weather_data.protection_methods import protection_methods, get_protection_explanation
from app.weather_data.weather_conditions import assess_weather_condition
from app.fertilizer_schedule import get_fertilizer_recommendation

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

def interpret_fertilizer(prediction, rainfall, previous_applications, location):
    ml_recommendation = fertilizer_recommendation_map[prediction]
    
    if ml_recommendation == 'Recommended':
        explanation = f"Based on the current rainfall ({rainfall} mm), fertilizing is generally recommended. The conditions are suitable for nutrient absorption without significant risk of leaching."
    else:
        if rainfall > 10:
            explanation = f"Due to heavy rainfall ({rainfall} mm), fertilizing is not recommended by the ML model. There's a high risk of nutrient leaching and potential water pollution."
        else:
            explanation = f"With low rainfall ({rainfall} mm), fertilizing is not recommended by the ML model. The soil might be too dry for effective nutrient absorption."
    
    schedule_recommendation = get_fertilizer_recommendation(previous_applications, location)
    
    return {
        "ml_recommendation": ml_recommendation,
        "ml_explanation": explanation,
        "next_application": schedule_recommendation
    }

