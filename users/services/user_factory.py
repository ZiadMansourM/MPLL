from abc import ABC, abstractmethod
from django.contrib.auth import get_user_model
from typing import Tuple

from users.forms import UserCreationForm
from .genpassword import generatePassword

CustomUser = get_user_model()

def _create_user(form: UserCreationForm):
    return CustomUser.objects.create(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )

class UserRegistrationStrategy(ABC):
    @abstractmethod
    def create_user(self, form: UserCreationForm) -> Tuple[str, CustomUser]:
        pass

class NormalRegistrationStrategy(UserRegistrationStrategy):
    def create_user(self, form: UserCreationForm) -> Tuple[str, CustomUser]:
        # [1]: create user
        user = _create_user(form)
        # [2]: Assign Password
        password = form.cleaned_data['password1']
        user.set_password(password)
        # [3]: Deactivate Account && save
        user.is_active = False
        user.save()
        return user.username, user

class ManagerRegistrationStrategy(UserRegistrationStrategy):
    def create_user(self, form: UserCreationForm) -> Tuple[str, CustomUser]:
        # [1]: create manager
        manager = _create_user(form)
        # [2]: Assign Password
        password = generatePassword()
        manager.set_password(password)
        # [3]: Define Type
        manager.is_manager = True
        # [4]: Deactivate Account && save
        manager.is_active = False
        manager.save()
        return password, manager

class EditorRegistrationStrategy(UserRegistrationStrategy):
    def create_user(self, form: UserCreationForm) -> Tuple[str, CustomUser]:
        # [1]: create editor
        editor = _create_user(form)
        # [2]: Assign Password
        password = generatePassword()
        editor.set_password(password)
        # [3]: Define Type
        editor.is_editor = True
        # [4]: Deactivate Account && save
        editor.is_active = False
        editor.save()
        return password, editor