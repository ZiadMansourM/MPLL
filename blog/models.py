import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .services.parser import cleanhtml
from PIL import Image
User = get_user_model()


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.CharField(_('Type'), max_length=20)
    url = models.URLField()
    message = RichTextField(blank=True, help_text=_(
        'If you want to leave a note for the reviewer'))
    date_reported = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.entity}:{self.url}"

    class Meta:
        db_table = 'reports'


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return f"{self.category}"

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "Categories"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120, unique=True)
    content = RichTextField()
    snippet = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    last_modifed = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(
        _('pinned status'),
        default=False,
        help_text=_('Designates whether the post is pinned'),
    )
    likes = models.ManyToManyField(User, related_name="liked_posts")
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name="categories",
        through="PostCategory",
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-is_pinned', '-date_posted']
        db_table = 'posts'

    def save(self, *args, **kwargs):
        self.snippet = cleanhtml(self.content)

        try:
            this = Post.objects.get(id=self.id)
            if this.image != self.image and this.image.name != "default.jpg":
                this.image.delete(save=False)
        except:
            pass

        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 900 or img.width >900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.image.path)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} -> {self.category.category}"

    class Meta:
        db_table = 'post_category'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_comments")

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return f"{self.post}-{self.owner}:{self.comment}"

    class Meta:
        db_table = 'comments'


class Reply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="replies")
    reply = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_replies")

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return f"{self.comment}-{self.owner}"

    class Meta:
        db_table = 'replies'
        verbose_name_plural = "Replies"


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_('email address'), help_text=_(
        'We will use this email to reach out to you.'))
    username = models.CharField(max_length=20, blank=True)
    message = models.TextField(help_text=_('Please provide your query here.'))
    date_sent = models.DateTimeField(default=timezone.now)
    is_urgent = models.BooleanField(
        _('urgent status'),
        default=False,
        help_text=_('Designates whether the request is URGENT.'),
    )

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'

    class Meta:
        db_table = 'contact_us'
        verbose_name_plural = "Contact Us"
