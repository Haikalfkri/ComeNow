from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser
from django import forms

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'text',
            })
        }