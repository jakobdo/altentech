from django.urls import path

from employee.views import EmployeeDetailView, EmployeeListView

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employees-list"),
    path(
        '<slug:slug>/',
        EmployeeDetailView.as_view(),
        name="employees-detail"
    ),
]
