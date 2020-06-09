from django.db import models

from client.models import Client
from employee.models import Employee
from technology.models import Technology


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    client = models.ForeignKey(
        Client,
        related_name="projects",
        on_delete=models.CASCADE
    )
    technologies = models.ManyToManyField(Technology)
    consultants = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name
