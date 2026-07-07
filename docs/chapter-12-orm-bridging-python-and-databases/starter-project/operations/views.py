from django.shortcuts import render

from .models import Project


def project_list_view(request):
    projects = Project.objects.select_related("customer").order_by("project_code")
    context = {"projects": projects, "title": "Project List"}
    return render(request, "operations/project_list.html", context)
