from .settings import BASE_DIR
from django.db import models
from pathlib import Path
import joblib

def load_model():
    path = Path(BASE_DIR).joinpath(Path('mnapi/files/model.pkl'))
    model = joblib.load(path)
    return model

def load_scaler():
    path = Path(BASE_DIR).joinpath(Path('mnapi/files/scaler.pkl'))
    scaler = joblib.load(path)
    return scaler
