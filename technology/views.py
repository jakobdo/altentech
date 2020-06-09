from django.views.generic import DetailView, ListView

from technology.models import Technology


class TechnologyDetailView(DetailView):
    model = Technology


class TechnologyListView(ListView):
    model = Technology
