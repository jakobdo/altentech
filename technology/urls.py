from django.urls import path

from technology.views import TechnologyDetailView, TechnologyListView

urlpatterns = [
    path('', TechnologyListView.as_view(), name="technologies-list"),
    path(
        '<slug:slug>/',
        TechnologyDetailView.as_view(),
        name="technologies-detail"
    ),
]
