from studio_app.models import *
from rest_framework import serializers

class GearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gear
        fields = '__all__'