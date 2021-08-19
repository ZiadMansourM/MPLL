from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

CustomUser = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

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