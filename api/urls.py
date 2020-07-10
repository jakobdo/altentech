from django.urls import path

from api import views

# from client.viewsets import ClientViewSet, IndustryViewSet
# from technology.viewsets import TechnologyViewSet

urlpatterns = [
    path('consultants/', views.ConsultantList.as_view(), name="api-consultant-list"),
    path('consultants/get_random/', views.ConsultantRandomDetail.as_view(), name="api-consultant-random-detail"),
    path('consultants/tags/<slug:slug>/', views.ConsultantList.as_view(), name="api-consultant-list"),
    path('consultants/<slug:slug>/', views.ConsultantDetail.as_view(), name="api-consultant-detail"),
    path('tags/', views.TagList.as_view(), name="api-tag-list"),
    path('projects/', views.ProjectList.as_view(), name="api-project-list"),
    path('projects/<slug:slug>/', views.ProjectDetail.as_view(), name="api-project-detail"),
    path('technologies/', views.TechnologyList.as_view(), name="api-technology-list"),
    path('technologies/<slug:slug>/', views.TechnologyDetail.as_view(), name="api-technology-detail"),
    path('areas/', views.AreaList.as_view(), name="api-area-list"),
    path('areas/<slug:slug>/', views.AreaDetail.as_view(), name="api-area-detail"),
]
