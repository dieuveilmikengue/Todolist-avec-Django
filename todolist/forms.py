from django.core import validators
from django import forms
from .models import Taches


class AddTask(forms.ModelForm):
    class Meta:
        model = Taches
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': '.input',
                'placeholder':"Veuillez ajoutez une tache",
                "spellcheck": "false"
            }),
            'description': forms.Textarea(attrs={
                'class': '.textarea',
                'placeholder':"Veuillez ajoutez une tache",
                "spellcheck": "false"
            })
        }