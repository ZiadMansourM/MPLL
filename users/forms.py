from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
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
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            "class": "form-control bg-light",
            'placeholder': 'Account password',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            "class": "form-control bg-light",
            'placeholder': 'Confirm Account password',
        }),
        help_text=_("Enter the same password as before, for verification."),
    )

    email = forms.EmailField(
        label=_("Email Address"),
        widget=forms.EmailInput(attrs={
            "class": "form-control bg-light",
            'placeholder': 'Primary Email',
        }),
        help_text=_("We will send an activation link to this email"),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'Account username'}),
            'first_name': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'Last name'}),
        }


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
    password1 = None
    password2 = None

    email = forms.EmailField(
        label=_("Email Address"),
        widget=forms.EmailInput(attrs={
            "class": "form-control bg-light",
            'placeholder': 'Primary Email',
        }),
        help_text=_("We will send an activation link to this email"),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'Account username'}),
            'first_name': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={"class": "form-control bg-light", 'placeholder': 'Last name'}),
        }