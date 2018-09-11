from studio_app.models import *
from rest_framework import serializers

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'