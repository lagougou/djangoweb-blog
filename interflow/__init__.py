from django.apps import AppConfig
import os

default_app_config = 'interflow.IndexConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '留言管理'