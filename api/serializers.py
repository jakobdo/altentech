from rest_framework import serializers
from stdimage_serializer.fields import StdImageField

from client.models import Client, Industry
from employee.models import Employee, Experience, TechnologyLevel
from project.models import Project
from tag.models import Tag
from technology.models import Technology


# Simplified serializers
class ClientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'slug']


class IndustrySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name', 'slug']


class TechnologySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name', 'slug']


class ProjectSimpleSerializer(serializers.ModelSerializer):
    technologies = TechnologySimpleSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'name',
            'slug',
            'technologies',
        ]


class ConsultantSimpleSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    image = StdImageField()

    class Meta:
        model = Employee
        fields = [
            'fullname',
            'image',
            'jobtitle',
            'slug'
        ]

    def get_fullname(self, obj):
        return obj.get_full_name()


# Full serializers
class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSimpleSerializer()
    industry = IndustrySimpleSerializer()
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


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'slug', 'description', 'url', 'image']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name', 'slug', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']


class TechnologySerializer(serializers.ModelSerializer):
    consultants = ConsultantSimpleSerializer(many=True)

    class Meta:
        model = Technology
        fields = ['name', 'slug', 'description', 'consultants']


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
    projects = ProjectSimpleSerializer(many=True)

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
            'experience',
            'projects'
        ]

    def get_fullname(self, obj):
        return obj.get_full_name()
