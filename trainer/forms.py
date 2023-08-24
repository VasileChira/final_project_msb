from django import forms
from django.forms import TextInput, EmailInput, Select
from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'departament', 'active', 'profile']

        widgets = {
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your course name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email here'}),
            'departament': Select(attrs={'class': 'form-select'}),
        }



class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'departament', 'active', 'profile']

        widgets = {
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your course name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email here'}),
            'departament': Select(attrs={'class': 'form-select'}),
        }