from rest_framework import viewsets
from django.core import serializers
from studio_app.models import *
from studio_app.serializers import *

class GearViewSet(viewsets.ModelViewSet):

    queryset = Gear.objects.all()
    serializer_class = GearSerializer