from django.contrib import admin

from collect.models import Collect


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    pass
