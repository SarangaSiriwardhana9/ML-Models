from flask import Blueprint, request, jsonify
from app.models import WeatherModel
from app.utils import prepare_input_data, interpret_watering, interpret_protection, interpret_fertilizer
from datetime import datetime

bp = Blueprint('main', __name__)
weather_model = WeatherModel()

@bp.route('/watering', methods=['POST'])
def predict_watering():
    try:
        data = request.json
        input_data = prepare_input_data(data, 'watering')
        
        watering_prediction = weather_model.predict_watering(input_data)
        
        response = {
            'location': data.get('Location', '').upper(),
            'watering_recommendation': interpret_watering(watering_prediction)
        }
        
        return jsonify(response)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@bp.route('/protection', methods=['POST'])
def predict_protection():
    try:
        data = request.json
        input_data = prepare_input_data(data, 'protection')
        
        protection_prediction = weather_model.predict_protection(input_data)
        
        response = {
            'location': data.get('Location', '').upper(),
            'protection_recommendations': interpret_protection(protection_prediction, data)
        }
        
        return jsonify(response)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@bp.route('/fertilizer', methods=['POST'])
def predict_fertilizer():
    try:
        data = request.json
        input_data = prepare_input_data(data, 'fertilizer')
        
        fertilizer_prediction = weather_model.predict_fertilizer(input_data)
        
        previous_applications = data.get('previous_applications', [])
        for app in previous_applications:
            app['date'] = datetime.strptime(app['date'], '%Y-%m-%d')
        
        response = {
            'location': data.get('Location', '').upper(),
            'fertilizer_recommendation': interpret_fertilizer(
                fertilizer_prediction, 
                data['Rainfall (mm)'],
                previous_applications,
                data.get('Location', '').upper()
            )
        }
        
        return jsonify(response)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

