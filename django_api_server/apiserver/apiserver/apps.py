from django.apps import AppConfig


class MnModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiserver'

    def ready(self):
        from .models import load_model, load_scaler
        self.model = load_model()
        self.scaler = load_scaler()
