import joblib
from config import Config

class WeatherModel:
    def __init__(self):
        self.watering_model = joblib.load(Config.WATERING_MODEL_PATH)
        self.protection_model = joblib.load(Config.PROTECTION_MODEL_PATH)
        self.multilabel_binarizer = joblib.load(Config.MULTILABEL_BINARIZER_PATH)

    def predict_watering(self, data):
        return self.watering_model.predict(data)[0]

    def predict_protection(self, data):
        prediction = self.protection_model.predict(data)
        return self.multilabel_binarizer.inverse_transform(prediction)[0]

