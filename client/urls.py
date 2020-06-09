from django.urls import path

from client.views import ClientDetailView, ClientListView

urlpatterns = [
    path('', ClientListView.as_view(), name="clients-list"),
    path(
        '<slug:slug>/',
        ClientDetailView.as_view(),
        name="clients-detail"
    ),
]
