from rest_framework.generics import ListAPIView, RetrieveAPIView

from employee.models import Employee
from employee.serializers import ConsultantSerializer
from project.models import Project
from project.serializers import ProjectSerializer
from tag.models import Tag
from tag.serializers import TagSerializer


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
