from django.urls import path,include
from user.customauth import CustomObtainAuthToken
from user.views import *
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'location', RetrieveLocation, basename='location')
app_name = 'users'

urlpatterns = [
    path('register/',CreateUser.as_view()),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('login/', CustomObtainAuthToken.as_view()),
    # path('location/',RetrieveLocation.as_view()),
]+router.urls
