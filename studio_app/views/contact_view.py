from rest_framework import viewsets
# from rest_framework.decorators import action
# from django.shortcuts import render, get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from django.http import HttpResponse
from studio_app.models import *
from studio_app.serializers import *


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer