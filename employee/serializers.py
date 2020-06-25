from rest_framework import serializers
from stdimage_serializer.fields import StdImageField

from employee.models import Employee, Experience, TechnologyLevel


class TechnologyLevelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='technology.id')
    name = serializers.ReadOnlyField(source='technology.name')
    slug = serializers.ReadOnlyField(source='technology.slug')

    class Meta:
        model = TechnologyLevel
        fields = ['id', 'name', 'slug', 'level']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['start', 'company', 'job_title', 'description']


class ConsultantSerializer(serializers.ModelSerializer):
    image = StdImageField()
    technologies = TechnologyLevelSerializer(
        source='technologylevel_set',
        many=True
    )
    experience = ExperienceSerializer(source='jobs', many=True)

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
            'experience'
        ]
