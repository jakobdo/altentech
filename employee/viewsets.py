from rest_framework import viewsets

from employee.models import Employee
from employee.serializers import ConsultantSerializer


class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = ConsultantSerializer
