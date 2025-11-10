from django.apps import AppConfig


class BoutiqueAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Boutique_app'

def ready(self):
        import Boutique_app.signals
