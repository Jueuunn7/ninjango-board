from django.apps import AppConfig
from ..domain import models


class CommentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "comment"
