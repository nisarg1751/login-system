# from dataclasses import fields
from pyexpat import model
from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class EditUserProfileForm(UserChangeForm):
    password1 = None
    password2 = None
    # password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','last_login','is_active']
        
