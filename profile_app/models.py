from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("Email is not Provided")
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, name, email, password):
        user = self.create_user(name=name, email=email, password=password)
        
        user.is_superuser = True
        user.is_staff = True
        
        return user

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