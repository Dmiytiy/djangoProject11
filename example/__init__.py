from django.apps import AppConfig

default_app_config = 'example.apps.ExampleConfig'


class ExampleConfig(AppConfig):
    name = 'example'

    def ready(self):
        # Здесь можно делать импорты моделей и тегов после загрузки приложений.
        from example.templatetags.menu_tags import draw_menu