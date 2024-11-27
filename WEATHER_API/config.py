import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    WATERING_MODEL_PATH = 'watering_random_forest_model.pkl'
    PROTECTION_MODEL_PATH = 'protection_method_model.pkl'
    MULTILABEL_BINARIZER_PATH = 'multilabel_binarizer.pkl'

