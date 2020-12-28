from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='First_Name')
    last_name = forms.CharField(required=True, label='Last_Name')


    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if len(value.strip())<4:
            raise ValidationError('The first_name must 4 char long..')
        else:
            return value.strip()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if len(value.strip())<4:
            raise ValidationError('The last_name must 4 char long..')
        else:
            return value.strip()

    class Meta:
        model = User
        fields = ['username','first_name','last_name']


