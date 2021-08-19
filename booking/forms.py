from django import forms
from .models import Book
from ckeditor.widgets import CKEditorWidget


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'classification', 'code',
                  'pages_num', 'date_published', 'date_added', 'publisher',
                  'available_copies', 'available_borrowing', 'available',
                  'image', 'brief']
