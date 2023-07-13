from django.apps import AppConfig
from django.contrib import admin
from .models import Question, Choice
from .models import Log


admin.site.register(Question)
admin.site.register(Choice)


class CatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"


class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp')
    search_fields = ('path', 'method')
    list_filter = ('method',)


admin.site.register(Log, LogAdmin)

