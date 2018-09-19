"""studioAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.views.static import serve
from django.conf.urls.static import static
from studio_app.views import *

router = routers.DefaultRouter()

router.register(r'manager', manager_view.ManagerViewSet, base_name='manager')
router.register(r'contact', contact_view.ContactViewSet, base_name='contact')
router.register(r'gear', gear_view.GearViewSet, base_name='gear')
router.register(r'meeting', meeting_view.MeetingViewSet, base_name='meeting')
router.register(r'session', session_view.SessionViewSet, base_name='session')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^register/', register_view.register_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
