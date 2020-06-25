from rest_framework import serializers

from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['pk', 'name', 'slug', 'description', 'client', 'industry']