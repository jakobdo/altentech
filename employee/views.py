from django.views.generic import DetailView, ListView

from employee.models import Employee
from tag.models import Tag


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeListView(ListView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        queryset = super(EmployeeListView, self).get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        return queryset.order_by('?')
