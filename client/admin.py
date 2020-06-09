from django.contrib import admin

from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Client, ClientAdmin)
