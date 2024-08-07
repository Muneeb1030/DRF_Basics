from rest_framework.serializers import ModelSerializer
from profile_app import models

class UserProfileSerializer(ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs ={
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }
        
    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        
        return user
    
class UserProfileFeedSerializer(ModelSerializer):
    class Meta:
        model = models.UserProfileFeed
        fields = ('id', 'user_profile', 'user_status', 'date_created')
        extra_kwargs = {'user_profile':{'read_only': True}}