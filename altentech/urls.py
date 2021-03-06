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

from base.views import AboutView, IndexView
from frontend.views import ReactIndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('consultants/', include('employee.urls')),
    path('projects/', include('project.urls')),
    path('clients/', include('client.urls')),
    path('technologies/', include('technology.urls')),
    path('about/', AboutView.as_view(), name="about-us"),
    path('react/', ReactIndexView.as_view(), name="react-index"),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('alten_dk_admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    ) + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
