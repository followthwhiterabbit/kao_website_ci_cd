from django.apps import AppConfig


class LeakTestingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leak_testing'
