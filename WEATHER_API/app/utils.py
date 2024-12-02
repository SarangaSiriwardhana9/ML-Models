import pandas as pd
from datetime import datetime
from app.weather_data.protection_methods import protection_methods, get_protection_explanation
from app.weather_data.weather_conditions import assess_weather_condition
from app.fertilizer_schedule import get_fertilizer_recommendation

# Mapping dictionaries with Sinhala translations for watering only
location_map = {
    'PUTTALAM': 0,
    'KURUNEGALA': 1
}

watering_frequency_map = {
    0: 'ජලය දැමීම අත්‍යවශ්‍ය නොවේ',
    1: 'ආසන්න වශයෙන් {water_used} L/m² බැගින් ජලය එක් වරක් ‍යොදන්න',
    2: 'ආසන්න වශයෙන් {water_used} L/m² බැගින් ජලය දෙවරක් ‍යොදන්න'
}

fertilizer_recommendation_map = {
    0: 'Not Recommended',
    1: 'Recommended'
}

# Helper functions
def prepare_input_data(data, model_type):
    location = data.get('Location', '').upper()
    if location not in location_map:
        raise ValueError('කරුණාකර පුත්තලම හෝ කුරුණෑගල ප්‍රදේශ පමනක් ඇතුලත් කරන්න.')

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
    watering_frequency = int(round(prediction[0]))
    water_used = round(prediction[1], 1)
    return watering_frequency_map[watering_frequency].format(water_used=water_used)

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
        explanation = f"වත්මන් වර්ෂාපතනය (මි.මී {rainfall}),මත පදනම්ව,මෙදින පොහොර යෙදීම සදහා බාදාවක් නොමැත. කාන්දු වීමේ සැලකිය යුතු අවදානමක් නොමැති හෙයින් පෝෂක අවශෝෂණය සුදුසු කාලගුණයක් ඇත"
    else:
        if rainfall > 10:
            explanation = f"අධික වර්ෂාපතනය (මි.මී.{rainfall}), හේතුවෙන් මෙදින අප විසින් පොහොර යෙදීම නිර්දේශ නොකරනු ලැබේ. මන්ද යත් පෝෂක කාන්දු වීම සහ ජලය දූෂණය වීමේ ඉහළ අවදානමක් පවතී.."
        else:
            explanation = f"උණූසුම් කාලගුණය හා අඩු වර්ශාපතනය හේතුවෙන් ({rainfall} mm), පොහොර දැමීම අප විසින් නිර්දේශ නොකරයි. මන්දයත් වියලි පස මගින් පෝශක අවශෝශනය එතරම් ඵ්ලදායී ලෙස සිදු නොවේ"

    schedule_recommendation = get_fertilizer_recommendation(previous_applications, location)
    
    return {
        "ml_recommendation": ml_recommendation,
        "ml_explanation": explanation,
        "next_application": schedule_recommendation
    }
