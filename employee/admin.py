from django.contrib import admin

from employee.models import Employee, Experience


class TechnologyLevelInline(admin.TabularInline):
    model = Employee.technologies.through


class ExperienceInline(admin.TabularInline):
    model = Experience


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstname", "lastname")}
    inlines = [
        TechnologyLevelInline,
        ExperienceInline,
    ]


admin.site.register(Employee, EmployeeAdmin)
