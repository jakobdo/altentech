from django.contrib import admin

from technology.models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Technology, TechnologyAdmin)
