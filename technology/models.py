from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "technologies"
        ordering = ['name']

    def __str__(self):
        return self.name
