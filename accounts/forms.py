from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields= ('email','name', 'phone', 'password1', 'password2')