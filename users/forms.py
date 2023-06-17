from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserRegistrationForm(UserCreationForm):
  
    class Meta:
    # Свойство модели User
        model = User
    # Свойство назначения полей
        fields = ('username',  'password1', 'password2', )
        
        

        

