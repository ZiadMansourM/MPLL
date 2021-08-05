from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    is_editor = models.BooleanField(
        _('editor status'),
        default=False,
        help_text=_('Designates whether the user can edit posts in blog.'),
    )
    class Meta:
        db_table = 'users'
