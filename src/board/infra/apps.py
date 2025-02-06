from django.apps import AppConfig
from ..domain import models


class BoardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "board"
