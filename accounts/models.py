# from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from djongo import models



# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, phone, password=None):
        """Create a new user"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, phone, password=None):
        """Create a new superuser"""
        user = self.create_user(email, name, phone, password)
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user        


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the app"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return f"{self.name} - {self.email}"




