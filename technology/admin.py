from django.contrib import admin

from technology.models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Technology, TechnologyAdmin)
