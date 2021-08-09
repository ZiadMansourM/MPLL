from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(default='default.jpg', upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # TODO: Look me up
    last_modifed = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['title']
        db_table = 'posts'

    # def save(self, *args, **kwargs):
    #     try:
    #         this = Post.objects.get(id=self.id)
    #         if this.image.name != self.image.name and this.image.name != "default.jpg":
    #             this.MyImageFieldName.delete()
    #     except: pass
    #     super(Post, self).save(*args, **kwargs)