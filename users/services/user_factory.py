from abc import ABC, abstractmethod
from django.contrib.auth import get_user_model
from .genpassword import generatePassword

CustomUser = get_user_model()

class UserRegistrationStrategy(ABC):
    @abstractmethod
    def create_user(self, username: str) -> str:
        pass


class ManagerRegistrationStrategy(UserRegistrationStrategy):
    def create_user(self, username: str) -> str:
        # [1]: create manager
        manager = CustomUser.objects.create(username=username)
        # [2]: Assign Password
        password = generatePassword()
        manager.set_password(password)
        # [3]: Define Type
        manager.is_manager = True
        # [4]: Deactivate Account && save
        # manager.is_active = False
        manager.save()
        return password

class EditorRegistrationStrategy(UserRegistrationStrategy):
    def create_user(self, username: str) -> str:
        # [1]: create editor
        editor = CustomUser.objects.create(username=username)
        # [2]: Assign Password
        password = generatePassword()
        editor.set_password(password)
        # [3]: Define Type
        editor.is_editor = True
        # [4]: Deactivate Account && save
        # editor.is_active = False
        editor.save()
        return password