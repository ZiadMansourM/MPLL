from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
        AuthenticationForm,
        UserCreationForm,
        UserChangeForm,
        UsernameField
    )
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CustomUser = get_user_model()


class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'autofocus': True, 
            "class": "form-control bg-light",
            'placeholder': 'Account username',
        }
    ))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password', 
                "class": "form-control bg-light",
                'placeholder': 'Account password',
            }
        ),
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'image', 'first_name', 'last_name', 'telephone']
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control bg-light"}),
            'last_name': forms.TextInput(attrs={"class": "form-control bg-light"}),
            'email': forms.EmailInput(attrs={"class": "form-control bg-light"}),
            'telephone': forms.TextInput(attrs={"class": "form-control bg-light"}),
        }

class MLERegisterForm(UserCreationForm): 
    # MLE : manager librarian editor
    # set password "1,2" to None to hide them from the form
    email = forms.EmailField(required=True)
    password1 = None 
    password2 = None 
    
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]