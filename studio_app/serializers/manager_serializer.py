from studio_app.models import *
from rest_framework import serializers

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('first_name', 'last_name', 'created', 'street_address', 'city', 'state', 'zipcode', 'id')