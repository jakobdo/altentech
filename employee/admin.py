from django.contrib import admin

from employee.models import Employee


class TechnologyLevelInline(admin.TabularInline):
    model = Employee.technologies.through


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstname", "lastname")}
    inlines = [
        TechnologyLevelInline,
    ]


admin.site.register(Employee, EmployeeAdmin)
