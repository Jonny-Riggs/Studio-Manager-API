from studio_app.models import *
from rest_framework import serializers

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'