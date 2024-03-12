from django.contrib import admin

from collect.models import Collect


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    readonly_fields = ['current_collect', 'people_donated']
