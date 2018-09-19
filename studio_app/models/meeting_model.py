from django.db import models
from studio_app.models import Manager

from django.contrib.auth.models import User


class Meeting(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
    )
    person = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    time = models.DateTimeField()
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.person