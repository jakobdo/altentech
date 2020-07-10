from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import (ConsultantSerializer, ProjectSerializer,
                             ServiceAreaSerializer,
                             ServiceAreaSimpleSerializer, TagSerializer,
                             TechnologySerializer)
from employee.models import Employee
from project.models import Project
from tag.models import ServiceArea, Tag
from technology.models import Technology


class ConsultantList(ListAPIView):
    serializer_class = ConsultantSerializer

    def get_queryset(self):
        queryset = Employee.objects.order_by('?')

        tag_slug = self.kwargs.get('slug')
        if tag_slug:
            try:
                tag = Tag.objects.get(slug=tag_slug)
                queryset = queryset.filter(tags=tag)
            except Tag.DoesNotExist:
                pass
        return queryset


class ConsultantDetail(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = ConsultantSerializer
    lookup_field = 'slug'


class ConsultantRandomDetail(RetrieveAPIView):
    queryset = Employee.objects.order_by('?')
    serializer_class = ConsultantSerializer

    def get_object(self):
        obj = self.queryset[0]
        self.check_object_permissions(self.request, obj)
        return obj


class TagList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class TechnologyList(ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TechnologyDetail(RetrieveAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    lookup_field = 'slug'


class AreaList(ListAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSimpleSerializer


class AreaDetail(RetrieveAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    lookup_field = 'slug'
