from django.apps import AppConfig


class ProducerConfig(AppConfig):
    name = 'producer'

    def ready(self):
        import producer.signals
