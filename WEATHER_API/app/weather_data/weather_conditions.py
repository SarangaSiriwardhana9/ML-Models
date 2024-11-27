def assess_weather_condition(weather_data):
    rainfall = weather_data.get('Rainfall (mm)', 0)
    max_temp = weather_data.get('Max Temp (°C)', 0)
    
    if rainfall > 10:
        return "Heavy Rain"
    elif max_temp > 30 and rainfall < 1:
        return "High Temperature, No Rain"
    else:
        return "Normal Conditions"

