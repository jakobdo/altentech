from django.db import models
from django.utils.translation import gettext
from stdimage import JPEGField

from technology.models import Technology


class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
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
            }
        }
    )
    technologies = models.ManyToManyField(
        Technology,
        through='TechnologyLevel'
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class TechnologyLevel(models.Model):
    class Levels(models.IntegerChoices):
        BEGINNER = 1, gettext('Beginner')
        INTERMEDIATE = 2, gettext('Intermediate')
        ADVANCED = 3, gettext('Advanced')
        __empty__ = gettext('(Unknown)')

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    level = models.SmallIntegerField(choices=Levels.choices)
