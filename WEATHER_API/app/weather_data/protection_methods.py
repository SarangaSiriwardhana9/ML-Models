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

def get_protection_explanation(method, weather_condition):
    explanations = {
        'Mulching': "Spread organic mulch around the base of the plants to retain soil moisture and reduce evaporation.",
        'Shading': "Use shade nets or temporary coverings to protect the plants from direct sunlight during peak hours.",
        'Frequent Watering': "Water the plants early in the morning or late in the evening to prevent dehydration. Use drip irrigation or sprinklers for efficient water distribution.",
        'Windbreaks': "Place temporary barriers around the field to reduce hot, dry winds that can stress the plants.",
        'Soil Enrichment': "Apply compost or organic manure to improve soil water-holding capacity and boost root development under stress.",
        'Drainage System': "Build small trenches or channels around the plants to quickly drain excess water and prevent waterlogging.",
        'Cover the Plants': "Use polythene sheets or temporary plastic tunnels to shield young plants from heavy rain, ensuring they remain upright.",
        'Stake the Plants': "Tie the plants to small stakes or sticks to prevent them from being uprooted or bent by strong winds and heavy rain.",
        'Sand Pillows (Bags)': "Place sandbags around the plant beds to reduce water infiltration and prevent the beds from filling with excess water during heavy rains.",
        'Avoid Over-Fertilizing': "Refrain from applying fertilizers during continuous rains as they may leach away, damaging the plants or polluting the soil.",
        'Inspect Regularly for Pests/Diseases': "Heavy rains often encourage fungal growth. Regularly inspect plants and apply organic fungicides if needed."
    }
    
    base_explanation = explanations.get(method, "No specific explanation available.")
    
    if weather_condition == "Heavy Rain":
        if method in ['Drainage System', 'Cover the Plants', 'Stake the Plants', 'Sand Pillows (Bags)', 'Avoid Over-Fertilizing', 'Inspect Regularly for Pests/Diseases']:
            return f"Due to heavy rain, {base_explanation.lower()}"
    elif weather_condition == "High Temperature, No Rain":
        if method in ['Mulching', 'Shading', 'Frequent Watering', 'Windbreaks', 'Soil Enrichment']:
            return f"Due to high temperature and lack of rain, {base_explanation.lower()}"
    
    return base_explanation

