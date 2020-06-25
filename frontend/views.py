from django.views.generic import TemplateView


class ReactIndexView(TemplateView):
    template_name = 'frontend/index.html'
