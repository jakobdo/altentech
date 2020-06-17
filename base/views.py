from django.views.generic import DetailView

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
