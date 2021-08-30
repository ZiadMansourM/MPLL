import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(default='default.jpg', upload_to='user_pics')
    is_editor = models.BooleanField(
        _('editor status'),
        default=False,
        help_text=_('Designates whether the user can edit posts in blog.'),
    )
    is_librarian = models.BooleanField(
        _('librarian status'),
        default=False,
        help_text=_('Designates whether the user can edit the book store database.'),
    )
    is_manager = models.BooleanField(
        _('manager status'),
        default=False,
        help_text=_('Designates whether the user is a manager'),
    )

    telephone = models.CharField(max_length=12, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return f"{self.username}"

    def save(self, *args, **kwargs):
        try:
            this = CustomUser.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: 
            pass
        super(CustomUser, self).save(*args, **kwargs)