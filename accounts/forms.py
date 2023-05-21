from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(max_length=15, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserProfile
        fields= ('email','name', 'phone', 'password1', 'password2')


  
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)


        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
