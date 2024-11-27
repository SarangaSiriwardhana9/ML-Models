import pandas as pd

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

def prepare_input_data(data):
    location = data.get('Location', '').upper()
    if location not in location_map:
        raise ValueError('Invalid location. Please use PUTTALAM or KURUNEGALA.')

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

def interpret_protection(prediction):
    return [protection_methods.get(method, method) for method in prediction]

