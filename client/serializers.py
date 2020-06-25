from rest_framework import serializers

from client.models import Client, Industry


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['pk', 'name', 'slug', 'description', 'url', 'image']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['pk', 'name', 'slug', 'description']
