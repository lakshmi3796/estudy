from django import forms
from Users.models import *

class StudentRegistrationForm(forms.Form):
	first_name=forms.CharField(max_length=200,required=True)
	last_name=forms.CharField(max_length=200,required=True)
	username=forms.CharField(max_length=200,required=True)
	email=forms.EmailField(max_length=200,required=True)
	password=forms.CharField(max_length=200,required=True,widget=forms.PasswordInput())
	confirm_password=forms.CharField(max_length=200,required=True,widget=forms.PasswordInput())

class StudentLoginForm(forms.Form):
	username=forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter Your username..'}))
	password=forms.CharField(max_length=200,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password..'}))
