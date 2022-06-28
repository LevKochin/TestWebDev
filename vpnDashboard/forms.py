from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': ''}
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'input__element',
                'style': 'width:326px;'
                         'height:48px;'
                         'border:0px;'
                         'border-radius:8px;'
                         'background-color:#1c1c1e;'
                         'margin-left:20px;'
                         'margin-bottom:10px',
                'placeholder': 'Name'
            }),
            'last_name': TextInput(attrs={
                'class': 'input__element',
                'style': 'width:326px;'
                         'height:48px;'
                         'border:0px;'
                         'border-radius:8px;'
                         'background-color:#1c1c1e;'
                         'margin-left:20px;'
                         'margin-bottom:10px',
                'placeholder': 'Surname'
            }),
            'email': EmailInput(attrs={
                'class': 'input__element',
                'style': 'width:326px;'
                         'height:48px;'
                         'border:0px;'
                         'border-radius:8px;'
                         'background-color:#1c1c1e;'
                         'margin-left:20px;'
                         'margin-bottom:10px',
                'placeholder': 'Email'
            })
        }
