from django.contrib import admin

from tag.models import ServiceArea, Tag


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


class ServiceAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Tag, TagAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
