from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from blog.parser import cleanhtml
# Create your models here.
# publisher.facebook
#


class SocialSite(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="accounts")
    handler = models.CharField(max_length=50)
    type = ForeignKey(SocialSite, on_delete=models.CASCADE,
                      related_name='accounts')

    def __str__(self):
        return self.account


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name_plural = "cities"


class Author(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(default='default.jpg', upload_to='site_pics')
    bio = models.TextField()
    birth_place = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="authors", blank=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=3)

    def __str__(self):
        return self.value


class Book(models.Model):

    section = models.ForeignKey(
        Code, on_delete=models.CASCADE, related_name="books")
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books", blank=True, null=True)
    pages_num = models.IntegerField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books", blank=True, null=True)
    available_copies = models.IntegerField(blank=True, null=True)
    available_borrowing = models.BooleanField()
    available = models.BooleanField()
    image = models.ImageField(default='default.jpg', upload_to='book_pics')
    brief= RichTextField()
    snippet=models.TextField()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.snippet = cleanhtml(self.brief)
        super(Book, self).save(*args, **kwargs)
