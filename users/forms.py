from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','name', 'first_name', 'email','password1', 'password2')