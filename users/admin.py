from django.contrib import admin
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(CustomUser)
class CustomUSerAdmin(UserAdmin):
    list_display = ('username', 'is_superuser',
                    'is_active', 'is_editor','is_librarian', 'is_manager')
    list_filter = ('is_superuser', 'is_active',
                   'is_editor','is_librarian', 'is_staff', 'is_manager')
    search_fields = ('username',)
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'email',
        )}),
        (_('Permissions'), {'fields': ('is_active',
                                       'is_staff',
                                       'is_superuser',
                                       'is_editor',
                                       'is_librarian',
                                       'is_manager',
                                       'groups',
                                       'user_permissions',
                                       )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',
                       'password1',
                       'password2',
                       'first_name',
                       'last_name',
                       'email',
                       'is_active',
                       'is_staff',
                       'is_superuser',
                       'is_editor',
                       'is_librarian',
                       'is_manager',
                       'groups',
                       'user_permissions',
                       )}
         ),
    )
