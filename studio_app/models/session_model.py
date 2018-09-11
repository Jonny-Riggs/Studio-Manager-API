from django.db import models
from studio_app.models import Manager, Gear

class Session(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
    )
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    reservation = models.DateTimeField()
    cost = models.IntegerField()
    reserved_gear = models.ForeignKey(
        Gear,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.artist