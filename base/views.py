from django.views.generic import DetailView, TemplateView

from employee.models import Employee


class IndexView(DetailView):
    model = Employee
    template_name = 'base/index.html'

    def get_object(self, queryset=None):
        try:
            obj = self.model.objects.order_by("?")[0]
        except IndexError:
            obj = None
        return obj


class AboutView(TemplateView):
    template_name = 'base/about.html'
