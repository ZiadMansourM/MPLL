from django.contrib import admin
from .models import Book, DeweyDecimalClassification, Author, Publisher, Account, SocialSite, City

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('classification', 'code', 'name', 'author', 'available', 'pages_num',
                    'date_published', 'date_added', 'publisher', 'available_copies', 'available_borrowing')
    list_filter = ('code', 'available', 'date_added',
                   'publisher', 'available_borrowing')
    # search_fields = ('')
    ordering = ('name',)
    exclude=('snippet',)


@admin.register(DeweyDecimalClassification)
class DeweyDecimalClassificationAdmin(admin.ModelAdmin):
    list_display = ('family', 'family_num')
    ordering = ('family_num',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'bio', 'birth_place')
    list_filter = ('birth_place',)
    # search_fields = ('')
    ordering = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone' )
    ordering = ('name',)

    def get_f(self, obj):   
        return obj.post.title
    get_f.admin_order_field = 'post'  # Allows column order sorting
    get_f.short_description = 'post title'  # Renames column head


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('publisher', 'handler','type')
    list_filter = ('handler','type')
    ordering = ('handler',)


@admin.register(SocialSite)
class SocialSiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
