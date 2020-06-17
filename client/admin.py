from django.contrib import admin

from client.models import Client, Industry


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Client, ClientAdmin)
admin.site.register(Industry, IndustryAdmin)
