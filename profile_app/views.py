from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from profile_app import serializers, models

class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    