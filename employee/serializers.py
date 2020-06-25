from rest_framework import serializers
from stdimage_serializer.fields import StdImageField

from employee.models import Employee, TechnologyLevel


class TechnologyLevelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='technology.id')
    name = serializers.ReadOnlyField(source='technology.name')

    class Meta:
        model = TechnologyLevel
        fields = ['id', 'name', 'level']


class ConsultantSerializer(serializers.ModelSerializer):
    image = StdImageField()
    technologies = TechnologyLevelSerializer(
        source='technologylevel_set',
        many=True
    )

    class Meta:
        model = Employee
        fields = [
            'pk',
            'firstname',
            'lastname',
            'slug',
            'jobtitle',
            'description',
            'teaser',
            'linkedin',
            'cv',
            'image',
            'technologies',
            'tags',
        ]
