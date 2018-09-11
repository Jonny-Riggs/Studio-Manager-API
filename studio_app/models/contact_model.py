from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .manager_model import Manager


class Contact(models.Model):
    studio_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')
    desc = models.CharField(max_length=250)


    def __str__(self):
        return self.first_name