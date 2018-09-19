from studio_app.models import *
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'desc', 'id', 'studio_manager')