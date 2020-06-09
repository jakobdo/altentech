from django.views.generic import DetailView, ListView

from employee.models import Employee


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeListView(ListView):
    model = Employee
