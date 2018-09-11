from django.db import models
from studio_app.models import Manager
from django.conf import settings

class Gear(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    accessories = models.CharField(max_length=200)
    specs = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
