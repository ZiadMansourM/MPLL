from django.contrib import admin
from .models import Post, Comment, Reply

# Register your models here.
admin.site.site_header = 'MPLL administration'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_pinned', 'date_posted')
    list_filter = ('author__username', 'is_pinned')
    search_fields = ('author__username', 'title')
    ordering = ('-date_posted',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_username', 'date_posted')
    list_filter = ('owner__username', 'post__title')
    search_fields = ('owner__username', 'post__title')
    ordering = ('-date_posted',)

    def get_title(self, obj):
        return obj.post.title
    get_title.admin_order_field = 'post'  #Allows column order sorting
    get_title.short_description = 'post title'  #Renames column head

    def get_username(self, obj):
        return obj.owner.username
    get_username.admin_order_field = 'owner'  #Allows column order sorting
    get_username.short_description = 'comment owner username'  #Renames column head

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_title', 'date_posted')
    list_filter = ('owner__username', 'comment__post__title')
    search_fields = ('owner__username', 'comment__post__title')
    ordering = ('-date_posted',)

    def get_title(self, obj):
        return obj.comment.post.title
    get_title.admin_order_field = 'comment'  #Allows column order sorting
    get_title.short_description = 'post title'  #Renames column head

    def get_username(self, obj):
        return obj.owner.username
    get_username.admin_order_field = 'owner'  #Allows column order sorting
    get_username.short_description = 'reply owner username'  #Renames column head

