from django.db import models
from studio_app.models import Manager

class Show(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE

    )
    venue = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    show_time = models.DateTimeField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.venue