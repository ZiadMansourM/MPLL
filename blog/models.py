from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from .parser import cleanhtml

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField()
    snippet = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # TODO: Look me up
    last_modifed = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(
        _('pinned status'),
        default=False,
        help_text=_('Designates whether the post is pinned'),
    )

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['title']
        db_table = 'posts'

    def save(self, *args, **kwargs):
        # try:
        #     this = Post.objects.get(id=self.id)
        #     if this.image.name != self.image.name and this.image.name != "default.jpg":
        #         this.MyImageFieldName.delete()
        # except: pass
        self.snippet = cleanhtml(self.content)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.post}-{self.owner}:{self.comment}"

    class Meta:
        db_table = 'comments'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    reply = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.comment}-{self.owner}"

    class Meta:
        db_table = 'replies'
        verbose_name_plural = "Replies"

class ContactUs(models.Model):
    # Basic Info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # Contact Info
    telephone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(_('email address'))
    # Data
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'
    
    class Meta:
        db_table = 'contact_us'
        verbose_name_plural = "Contact Us"