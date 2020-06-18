from django.urls import reverse
from django.utils.translation import gettext_lazy


def links(request):
    data = [
        dict(
            text=gettext_lazy("Consultants"),
            url=reverse('employees-list'),
            active=False
        ),
        dict(
            text=gettext_lazy("Projects"),
            url=reverse('projects-list'),
            active=False
        ),
        dict(
            text=gettext_lazy("Technologies"),
            url=reverse('technologies-list'),
            active=False
        ),
        dict(
            text=gettext_lazy("Contact Us"),
            url=reverse('contact-us'),
            active=False
        )
    ]

    path = request.path

    for link in data:
        current_link = link.get('url')
        if path == current_link or path.startswith(current_link):
            link['active'] = True

    context = {
        'links': data,
    }
    return context
