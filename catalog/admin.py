from django.apps import AppConfig
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)


class CatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"
