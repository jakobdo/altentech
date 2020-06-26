from rest_framework import viewsets
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import ConsultantSerializer


class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('?')
    serializer_class = ConsultantSerializer

    def retrieve(self, request, pk):
        if pk == '0':
            instance = self.queryset.first()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super().retrieve(request, pk)
