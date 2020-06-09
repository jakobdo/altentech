from django.views.generic import DetailView, ListView

from project.models import Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectListView(ListView):
    model = Project
