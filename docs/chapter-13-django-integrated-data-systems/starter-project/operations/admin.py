from django.contrib import admin

from .models import Customer, Project, WorkItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_code", "name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("customer_code", "name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_code", "name", "customer", "status")
    list_filter = ("status",)
    search_fields = ("project_code", "name")


@admin.register(WorkItem)
class WorkItemAdmin(admin.ModelAdmin):
    list_display = ("project", "title", "owner", "is_done")
    list_filter = ("is_done",)
    search_fields = ("title", "owner")
