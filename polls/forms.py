from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'description', 'expires_at', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your poll question'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional description'}),
            'expires_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }