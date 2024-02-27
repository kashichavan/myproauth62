from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())