from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.name
