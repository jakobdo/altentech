from rest_framework import serializers

from employee.serializers import ConsultantSimpleSerializer
from project.models import Project
from technology.serializers import TechnologySimpleSerializer


class ProjectSerializer(serializers.ModelSerializer):
    industry = serializers.CharField(source='industry.name')
    consultants = ConsultantSimpleSerializer(many=True)
    technologies = TechnologySimpleSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'name',
            'slug',
            'description',
            'client',
            'industry',
            'technologies',
            'consultants'
        ]
