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
    technologyLevels = TechnologyLevelSerializer(
        source='technologylevel_set',
        many=True
    )
    experience = ExperienceSerializer(source='jobs', many=True)
    fullname = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'firstname',
            'lastname',
            'fullname',
            'slug',
            'jobtitle',
            'description',
            'teaser',
            'linkedin',
            'cv',
            'image',
            'technologyLevels',
            'tags',
            'experience'
        ]

    def get_fullname(self, obj):
        return obj.get_full_name()


class ConsultantSimpleSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'fullname',
            'slug',
        ]

    def get_fullname(self, obj):
        return obj.get_full_name()
