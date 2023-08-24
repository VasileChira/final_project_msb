from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, TextInput, EmailInput

from student.models import Student


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter your username here'})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Enter your password'})


class ChardField:
    pass


class UserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['first_name','last_name', 'email',
                  # 'username'
                  ]
        widgets = {
            'first_name': TextInput(attrs ={'class':'form-control', 'placeholder': 'Enter your first name here'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}),
            # 'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),

        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your password'})



