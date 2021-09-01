from django.contrib import auth
from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from blog.services.parser import cleanhtml
from django.urls import reverse
# Create your models here.


class SocialSite(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    telephone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-list')


class Account(models.Model):
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="accounts")
    handler = models.CharField(max_length=50)
    type = ForeignKey(SocialSite, on_delete=models.CASCADE,
                      related_name='accounts')

    def __str__(self):
        return self.handler


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
    bio = models.TextField(blank=True)
    birth_place = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="authors",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

# TODO:reverse to detail view
    def get_absolute_url(self):
        return reverse('author-list')

    def save(self, *args, **kwargs):
        try:
            this = Author.objects.get(id=self.id)
            if this.image != self.image and this.image.name != "default.jpg":
                this.image.delete(save=False)
        except:
            pass

        super(Author, self).save(*args, **kwargs)


class DeweyDecimalClassification(models.Model):
    family = models.CharField(max_length=50,unique=True)
    family_num = models.CharField(max_length=3,unique=True)

    def __str__(self):
        return self.family_num


class Book(models.Model):

    classification = models.ForeignKey(
        DeweyDecimalClassification, on_delete=models.CASCADE, related_name="books")
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
    brief = RichTextField()
    snippet = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.snippet = cleanhtml(self.brief)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
