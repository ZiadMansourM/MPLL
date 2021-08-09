from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # TODO: Look me up
    last_modifed = models.DateTimeField(auto_now=True)