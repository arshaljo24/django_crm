from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'First Name'}))
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Last Name'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Email'}))
