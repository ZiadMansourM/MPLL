from django.contrib import admin
from .models import Post, Comment, Reply, ContactUs, Report
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

# Register your models here.
admin.site.site_header = 'MPLL administration'


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('entity', 'active_url', 'message', 'date_reported')
    list_filter = ('entity',)
    ordering = ('-date_reported',)

    def active_url(self, obj):
        return mark_safe(f'<a href="{obj.url}">{obj.url}</a>')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_pinned', 'date_posted')
    list_filter = ('author__username', 'is_pinned')
    search_fields = ('author__username', 'title')
    ordering = ('-date_posted',)
    fieldsets = (
        (_('Post info'), {'fields': (
            'title',
            'content',
            'image',
            'is_pinned',
        )}),
        (_('meta'), {'fields': (
            'author',
            'date_posted',
        )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',
                       'content',
                       'author',
                       'image',
                       'date_posted',
                       'is_pinned',
                       )}
         ),
    )
    exclude = ('snippet',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_username', 'comment', 'date_posted')
    list_filter = ('owner__username', 'post__title')
    search_fields = ('owner__username', 'post__title')
    ordering = ('-date_posted',)

    def get_title(self, obj):
        return obj.post.title
    get_title.admin_order_field = 'post'  # Allows column order sorting
    get_title.short_description = 'post title'  # Renames column head

    def get_username(self, obj):
        return obj.owner.username
    get_username.admin_order_field = 'owner'  # Allows column order sorting
    get_username.short_description = 'comment owner username'  # Renames column head


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_title', 'reply', 'date_posted')
    list_filter = ('owner__username', 'comment__post__title')
    search_fields = ('owner__username', 'comment__post__title')
    ordering = ('-date_posted',)

    def get_title(self, obj):
        return obj.comment.post.title
    get_title.admin_order_field = 'comment'  # Allows column order sorting
    get_title.short_description = 'post title'  # Renames column head

    def get_username(self, obj):
        return obj.owner.username
    get_username.admin_order_field = 'owner'  # Allows column order sorting
    get_username.short_description = 'reply owner username'  # Renames column head


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('get_fullname', 'is_urgent', 'message', 'date_sent')
    list_filter = ('is_urgent',)
    ordering = ('-date_sent',)

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"
