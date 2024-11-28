from datetime import datetime, timedelta

def get_fertilizer_type(year, month, day, location):
    if year not in [2023, 2024]:
        return None
    
    if month in [3, 4]:
        return "ගොම පොහොර" if location.upper() == "PUTTALAM" else "කොම්පෝස්ට්"
    elif month in [5, 6] and day in [1, 15]:
        return "NPK පොහොර (10-10-10) අනුපාතයට"
    elif month in [7, 8] and day == 1:
        return "සත්ව අපද්‍රව්‍ය"
    elif month in [9, 10] and day == 1:
        return "NPK පොහොර (10-10-10) අනුපාතයට"
    elif month in [11, 12, 1, 2] and day == 1:
        return "ග්ලිරිසීඩියා පත්‍ර"
    else:
        return None

def get_next_fertilizer_date(last_application_date):
    next_date = last_application_date + timedelta(days=1)
    while get_fertilizer_type(next_date.year, next_date.month, next_date.day, "PUTTALAM") is None:
        next_date += timedelta(days=1)
    return next_date

def get_fertilizer_recommendation(previous_applications, location):
    if not previous_applications:
        today = datetime.now()
        next_date = get_next_fertilizer_date(today)
    else:
        last_application = max(previous_applications, key=lambda x: x['date'])
        next_date = get_next_fertilizer_date(last_application['date'])
    
    fertilizer_type = get_fertilizer_type(next_date.year, next_date.month, next_date.day, location)
    
    return {
        'next_application_date': next_date.strftime('%Y-%m-%d'),
        'fertilizer_type': fertilizer_type
    }

