from django.apps import AppConfig


class MainVKAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_vk_app'
    #
    # def ready(self):
    #     from . import pars_vk_test
    #     pars_vk_test.execute()
