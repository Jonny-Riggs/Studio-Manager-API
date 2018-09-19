from studio_app.models import *
from rest_framework import serializers

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('brand', 'model', 'description', 'accessories', 'specs', 'image', 'id', 'studio_manager')