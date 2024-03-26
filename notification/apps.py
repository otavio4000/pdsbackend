from django.apps import AppConfig


class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'
    
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals