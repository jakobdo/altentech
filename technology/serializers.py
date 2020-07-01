from rest_framework import serializers

from technology.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name', 'slug', 'description']


class TechnologySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name', 'slug']
