from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters
from profile_app import serializers, models, permissions
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
class UserLoginApiViewSet(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    
class UserProfileFeedViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileFeedSerializer
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    queryset = models.UserProfileFeed.objects.all()
    authentication_classes = (TokenAuthentication,)
    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
