from rest_framework import serializers
from stdimage_serializer.fields import StdImageField

from employee.models import Employee


class ConsultantSerializer(serializers.ModelSerializer):
    image = StdImageField()

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
            'image'
        ]
