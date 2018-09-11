from studio_app.models import *
from rest_framework import serializers

class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'