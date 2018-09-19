from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers

from studio_app.models import *
from studio_app.serializers import *

class ManagerViewSet(viewsets.ModelViewSet):

    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    # def list(self, request):
    #     profile = Manager.objects.filter(Manager__user=self.request.user)
    #     valid_profile = get_object_or_404(profile, user=self.request.user)
    #     serializer = ManagerSerializer(valid_profile, context={'request': request})
    #     return Response(serializer.data)

