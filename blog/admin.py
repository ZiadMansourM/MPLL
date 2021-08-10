from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('author__username',)
    search_fields = ('author__username', 'title')
    ordering = ('-date_posted',)
