from rest_framework import viewsets
from django.core import serializers
from studio_app.models import *
from studio_app.serializers import *

class SessionViewSet(viewsets.ModelViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer