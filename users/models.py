import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image
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
            if this.image != self.image and this.image.name != "default.jpg":
                this.image.delete(save=False)
        except: 
            pass

        super(CustomUser, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 100 or img.width >100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)