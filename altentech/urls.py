"""altentech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from base.views import ContactView, IndexView
from client.viewsets import ClientViewSet
from employee.viewsets import ConsultantViewSet
from frontend.views import ReactIndexView
from project.viewsets import ProjectViewSet
from tag.viewsets import TagViewSet
from technology.viewsets import TechnologyViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'consultants', ConsultantViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('consultants/', include('employee.urls')),
    path('projects/', include('project.urls')),
    path('clients/', include('client.urls')),
    path('technologies/', include('technology.urls')),
    path('about/', ContactView.as_view(), name="about-us"),
    path('react/', ReactIndexView.as_view(), name="react-index"),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('alten_dk_admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    ) + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
