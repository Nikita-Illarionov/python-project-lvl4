from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, label='Имя')
    last_name = forms.CharField(max_length=254, label='Фамилия')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2',)
