from rest_framework import viewsets

from technology.models import Technology
from technology.serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
