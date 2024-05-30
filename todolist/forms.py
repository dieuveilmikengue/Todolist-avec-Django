from django.core import validators
from django import forms
from .models import Taches


class AddTask(forms.ModelForm):
    class Meta:
        model = Taches
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Veuillez ajoutez une tache"
            })
        }