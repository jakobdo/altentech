from django.db import models

from client.models import Client


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(
        Client,
        related_name="projects",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
