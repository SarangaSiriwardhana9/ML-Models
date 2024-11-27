from flask import Blueprint, request, jsonify
from app.models import WeatherModel
from app.utils import prepare_input_data, interpret_watering, interpret_protection

bp = Blueprint('main', __name__)
weather_model = WeatherModel()

@bp.route('/watering', methods=['POST'])
def predict_watering():
    try:
        data = request.json
        input_data = prepare_input_data(data)
        
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
        input_data = prepare_input_data(data)
        
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

