from studio_app.models import *
from rest_framework import serializers

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'