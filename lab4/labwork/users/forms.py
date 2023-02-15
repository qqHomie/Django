from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'last name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')