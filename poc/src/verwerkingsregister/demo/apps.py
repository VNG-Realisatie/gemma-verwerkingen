from django.apps import AppConfig


class DemoConfig(AppConfig):
    name = 'verwerkingsregister.demo'

    def ready(self):
        from . import signals