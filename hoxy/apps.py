from django.apps import AppConfig
import time

class HoxyConfig(AppConfig):
    name = 'hoxy'
    verbose_name='Hoxy?'

    def ready(self) : 
        from .tasks import db_update
        db_update.delay()
    