from rest_framework import viewsets
from studio_app.models import *
from studio_app.serializers import *

class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer