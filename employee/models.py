from django.core.validators import FileExtensionValidator
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
    teaser = models.CharField(max_length=100, null=True)
    linkedin = models.URLField(blank=True, null=True)
    cv = models.FileField(
        upload_to='cv/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        null=True
    )
    image = JPEGField(
        upload_to='employee/',
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
        through='TechnologyLevel',
        related_name='consultants'
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
        FUNDAMENTAL = 1, gettext('Fundamental')
        BEGINNER = 2, gettext('Beginner')
        INTERMEDIATE = 3, gettext('Intermediate')
        ADVANCED = 4, gettext('Advanced')
        EXPERT = 5, gettext('Expert')
        __empty__ = gettext('(Unknown)')

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    level = models.SmallIntegerField(choices=Levels.choices)

    class Meta:
        ordering = ['-level', 'technology__name']

    def __str__(self):
        return f"{self.technology} - {self.level}"


class Experience(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    start = models.DateField()
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['-start']

    def __str__(self):
        return f"{self.company} - {self.job_title}"
