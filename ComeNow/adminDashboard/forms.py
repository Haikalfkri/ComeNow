from django import forms
from events.models import EventModel


class CreateEventForm(forms.ModelForm):
    event_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
        'type': 'datetime-local',
        'id': 'event_date'
    }))
    
    
    class Meta:
        model = EventModel
        fields = ('name', 'description', 'location', 'image', 'contact', 'event_date', 'event_category', 'more_information')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'name',
                'placeholder': 'name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'id': 'description',
                'placeholder': 'description'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'location',
                'placeholder': 'location'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'type': 'file',
                'id': 'formFile'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'contact',
                'placeholder': 'contact'
            }),
            'event_category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'category'
            }),
            'more_information': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'more-information',
                'placeholder': '( optional )'
            })
        }