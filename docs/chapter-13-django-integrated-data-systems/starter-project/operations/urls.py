from django.urls import path

from .views import project_list_view

urlpatterns = [
    path("projects/", project_list_view, name="project-list"),
]
