from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from app_users.models import *


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия'
    }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'readonly': True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Почта',
        'readonly': True
    }))

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'avatar', 'username', 'email'
        )


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Почта'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2'
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class BookingForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия',
    }))
    date_entry = forms.CharField(widget=forms.TextInput())
    date_exit = forms.CharField(widget=forms.TextInput())
    
    class Meta:
        models = BookingRoom
        fields = (
            'first_name',
            'last_name',
            'date_entry',
            'date_exit'
        )