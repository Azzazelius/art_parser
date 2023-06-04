from django.apps import AppConfig


class ArtParserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'art_parser_app'
    #
    # def ready(self):
    #     from . import pars_vk_test
    #     pars_vk_test.execute()
