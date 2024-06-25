from django import forms

from .models import Posts

class UserPost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('body', )
        
        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Type something...'
            })
        }   