from django.views.generic import DetailView

from employee.models import Employee


class IndexView(DetailView):
    model = Employee
    template_name = 'base/index.html'

    def get_object(self, queryset=None):
        return self.model.objects.order_by("?")[0]
