from django.db import models

from client.models import Client, Industry
from employee.models import Employee
from technology.models import Technology


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    client = models.ForeignKey(
        Client,
        related_name="projects",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    industry = models.ForeignKey(
        Industry,
        related_name="projects",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    technologies = models.ManyToManyField(Technology)
    consultants = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name

    def get_client_or_industry(self):
        if self.client:
            return self.client.name
        elif self.industry:
            return self.industry.name
        else:
            return None
