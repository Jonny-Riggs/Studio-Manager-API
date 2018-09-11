from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers

from studio_app.models import *
from studio_app.serializers import *

class ManagerViewSet(viewsets.ModelViewSet):

    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

