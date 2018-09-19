from studio_app.models import *
from rest_framework import serializers

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('person', 'place', 'time', 'description', 'id', 'studio_manager')