from django.db import models
from .manager_model import Manager

from django.contrib.auth.models import User


class Contact(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    desc = models.CharField(max_length=250, blank=True)


    def __str__(self):
        return self.first_name