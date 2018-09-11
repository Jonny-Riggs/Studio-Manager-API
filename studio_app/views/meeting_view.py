from rest_framework import viewsets
from django.core import serializers
from studio_app.models import *
from studio_app.serializers import *

class MeetingViewSet(viewsets.ModelViewSet):

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer