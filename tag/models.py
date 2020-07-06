from django.db import models
from stdimage.models import JPEGField


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ServiceArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    image = JPEGField(
        upload_to='service_area/',
        variations={
            'full': {
                "width": None,
                "height": None
            },
            'thumbnail': {
                "width": 100,
                "height": 100,
                "crop": True
            },
            'medium': {
                "width": 300,
                "height": 300,
                "crop": True
            }
        }
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
