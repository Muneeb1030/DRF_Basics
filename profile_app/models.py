from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is not Provided")
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, name=name, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(name, email, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.name
    
    def get_full_name(self):
        return self.name
    
    
class UserProfileFeed(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_status =  models.CharField(max_length=254)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user_status