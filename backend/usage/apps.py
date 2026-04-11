from django.apps import AppConfig


class UsageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usage'


    def ready(self):
        import usage.signals
