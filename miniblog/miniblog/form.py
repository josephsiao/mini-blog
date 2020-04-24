from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Account',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter account',
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )

    password2 = forms.CharField(
        label='Password Again',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password again'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Account',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter account',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )
