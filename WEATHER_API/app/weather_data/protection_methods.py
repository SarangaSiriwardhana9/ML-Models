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
    'PI': 'Inspect Regularly for Pests/Diseases',
    'NP': 'No Protection'
    
}

def get_protection_explanation(method, weather_condition):
    explanations = {
        'Mulching': "පාංශු තෙතමනය රඳවා ගැනීමට සහ වාෂ්පීකරණය අඩු කිරීමට ශාක පාමුල කාබනික වසුන් ව්‍යාප්ත කරන්න.",
        'Shading': "දැඩි සෘජු හිරු එළියෙන් ශාක ආරක්ෂා කිරීම සඳහා සෙවන දැල් හෝ තාවකාලික ආවරණ භාවිතා කරන්න.",
        'Frequent Watering': "විජලනය වැළැක්වීම සඳහා උදේ හෝ සවස් වරුවේ පැලවලට වතුර දමන්න. කාර්යක්ෂම ජලය බෙදා හැරීම සඳහා බිංදු ජල ඉසීම හෝ ජල විදිනයක් භාවිතා කරන්න.",
        'Windbreaks': "උණුසුම් හා වියලි සුළං මගින් පැල වලට ඇතිවිය හැකි ආතතිය අවම කිරීම සදහා ක්ෂේත්‍රය වටා තාවකාලික බාධක තබන්න ",
        'Soil Enrichment': "පසෙහි ජලය රඳවා ගැනීමේ හැකියාව වැඩි දියුණු කිරීමට සහ ආතතිය යටතේ මුල් වර්ධනය වැඩි කිරීමට කැප්පෙටියා පත්‍ර හෝ ග්ලිරිසීඩියා පත්‍ර යොදන්න.",
        'Drainage System': "වර්ශාපතනය හේතුවෙන් අතිරික්ත ජලය ඉක්මනින් බැස යාමට සහ ජලයෙන් යටවීම වැළැක්වීමට ශාක වටා කුඩා අගල් හෝ කානු ගොඩනගන්න .",
        'Cover the Plants': "තද වර්ෂාපතනයෙන් අලුත් පැල ආරක්ෂා කර ගැනීම සඳහා පොලිතින් උර හෝ තාවකාලික ප්ලාස්ටික් උමං භාවිතා කරන්න, ඒවා කෙළින් පවතින බව සහතික කරන්න.",
        'Stake the Plants': "තද සුළං සහ අධික වර්ෂාවෙන් පැල කැඩීයාම හෝ  හෝ නැමීම වැළැක්වීම සඳහා තාවකාලිකව කුඩා කණුවලට හෝ කූරුවලට බැඳ තබන්න.",
        'Sand Pillows (Bags)': "අධික වර්ෂාව හේතුවෙන් පාත්ති අතිරික්ත ජලයෙන් පිරී යාම වැළැක්වීම අවම කිරීම සඳහා වැලි පුරවන ලද උර පැල වලට හානි නොවන සේ පාත්තිය තුලට යොදන්න ",
        'Avoid Over-Fertilizing': "Refrain from applying fertilizers during continuous rains as they may leach away, damaging the plants or polluting the soil.",
        'Inspect Regularly for Pests/Diseases': "අධික වර්ෂාව බොහෝ විට දිලීර වර්ධනයට හේතුවේ. නිරන්තර ශාක පරීක්ෂා කර අවශ්ය නම් කාබනික දිලීර නාශක යොදන්න.",
        'No Protection': "බුලත් වගාව සදහා අවශ්‍ය සාමාන්‍ය කාලගුණ තත්වයන් පැවතීම හේතුවෙන් අමතර ආරක්ශක උපක්‍රමයන් අවශ්‍ය නොවේ"
    }
    
    base_explanation = explanations.get(method, "No specific explanation available.")
    
    if weather_condition == "Heavy Rain":
        if method in ['Drainage System', 'Cover the Plants', 'Stake the Plants', 'Sand Pillows (Bags)', 'Avoid Over-Fertilizing', 'Inspect Regularly for Pests/Diseases']:
            return f"Due to heavy rain, {base_explanation.lower()}"
    elif weather_condition == "High Temperature, No Rain":
        if method in ['Mulching', 'Shading', 'Frequent Watering', 'Windbreaks', 'Soil Enrichment']:
            return f"Due to high temperature and lack of rain, {base_explanation.lower()}"
    
    return base_explanation

