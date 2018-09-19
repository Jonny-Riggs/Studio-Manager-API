from studio_app.models import *
from rest_framework import serializers

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('artist', 'genre', 'reservation', 'cost', 'id', 'studio_manager')