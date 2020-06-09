from django.urls import path

from project.views import ProjectDetailView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name="projects-list"),
    path(
        '<slug:slug>/',
        ProjectDetailView.as_view(),
        name="projects-detail"
    ),
]
