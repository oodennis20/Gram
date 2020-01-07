from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

# importing signals for the app to use in creating profile page automatically
    def ready(self):
        import images.signals