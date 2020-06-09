from django.views.generic import DetailView, ListView

from client.models import Client


class ClientDetailView(DetailView):
    model = Client


class ClientListView(ListView):
    model = Client
