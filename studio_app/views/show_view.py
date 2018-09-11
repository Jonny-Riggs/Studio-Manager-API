from rest_framework import viewsets
from django.core import serializers
from studio_app.models import *
from studio_app.serializers import *

class ShowViewSet(viewsets.ModelViewSet):

    queryset = Show.objects.all()
    serializer_class = ShowSerializer