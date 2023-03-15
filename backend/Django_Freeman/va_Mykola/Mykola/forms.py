from django import forms
from .models import *


class RegisterPostForm(forms.Form):
    person_email = forms.EmailField(max_length=250, label='Логін(Електронна пошта)')
    person_password = forms.CharField(max_length=30, label='Пароль')
