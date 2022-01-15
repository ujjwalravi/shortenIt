from django import forms
from django.forms import ModelForm
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UrlShortForm(ModelForm):
    class Meta:
        model = UrlShort
        fields = ('original',)
        widgets = {
            'original': forms.TextInput(attrs={'class': 'form-control', 'name': 'original', 'value': ""}),
        }

class UpdateUrlForm(ModelForm):
    class Meta:
        model = UrlShort
        fields = ('short',)

class CustomUrlForm(ModelForm):
    class Meta:
        model = UrlShort
        fields = ['original', 'short']
        widgets = {
            'original': forms.TextInput(attrs={'class': 'form-control', 'name': 'original', 'value': ""}),
            'short': forms.TextInput(attrs={'class': 'form-control', 'name': 'short', 'value': ""}),
        }

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form__input', 'type':'password', 'placeholder':'Password', 'name': 'password1'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form__input', 'type':'password', 'placeholder':'Confirm Password', 'name': 'password2'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
			'username': forms.TextInput(attrs={'class': 'form__input', 'name': 'username',  'placeholder': 'Username'}),
			'email': forms.TextInput(attrs={'class': 'form__input', 'name': 'email', 'placeholder': 'Email'}),
		}