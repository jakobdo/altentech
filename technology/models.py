from django.db import models

from tag.models import ServiceArea


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    service_areas = models.ManyToManyField(ServiceArea, related_name='technologies')

    class Meta:
        verbose_name_plural = "technologies"
        ordering = ['name']

    def __str__(self):
        return self.name
