from django.db import models
from studio_app.models import Manager
from django.conf import settings
from django.contrib.auth.models import User

class Gear(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    accessories = models.CharField(max_length=200)
    specs = models.CharField(max_length=200)
    image = models.CharField(max_length=60000)

    def __str__(self):
        return self.name
