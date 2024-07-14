from django.urls import path, include
from profile_app import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', viewset=views.UserProfileViewSet, basename='user-profile-viewset')

urlpatterns = [
    path('login', view=views.UserLoginApiViewSet.as_view()),
    path('', include(router.urls))
]
