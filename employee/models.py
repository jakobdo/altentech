from django.db import models
from django.utils.translation import gettext
from stdimage import JPEGField

from tag.models import Tag
from technology.models import Technology


class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    jobtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = JPEGField(
        upload_to='employee',
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
    technologies = models.ManyToManyField(
        Technology,
        through='TechnologyLevel'
    )
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['firstname', 'lastname']

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.get_full_name()


class TechnologyLevel(models.Model):
    class Levels(models.IntegerChoices):
        BEGINNER = 1, gettext('Beginner')
        INTERMEDIATE = 3, gettext('Intermediate')
        ADVANCED = 5, gettext('Advanced')
        __empty__ = gettext('(Unknown)')

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    level = models.SmallIntegerField(choices=Levels.choices)

    class Meta:
        ordering = ['-level', 'technology__name']
