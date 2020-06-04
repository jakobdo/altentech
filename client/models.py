from django.db import models
from stdimage import JPEGField


class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = JPEGField(
        upload_to='client',
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

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
