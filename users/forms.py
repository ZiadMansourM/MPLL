from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser

# TODO : AttributeError: 'str' object has no attribute '_meta'
# User = settings.AUTH_USER_MODEL


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class MLERegisterForm(UserCreationForm): 
    # MLE : manager librarian editor
    # set password "1,2" to None to hide them from the form
    password1 = None 
    password2 = None 
    
    class Meta:
        model = CustomUser # form.save
        fields = [
            'username',
            'first_name',
            'last_name'
        ]