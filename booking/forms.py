from django import forms
from .models import Book, Author, City, DeweyDecimalClassification, Publisher
from ckeditor.widgets import CKEditorWidget


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name', 'author', 'classification', 'code',
            'pages_num', 'date_published', 'date_added', 'publisher',
            'available_copies', 'available_borrowing', 'available',
            'image', 'brief'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. How to sleep', "class": "form-control"}),
            'author': forms.Select(choices=Author.objects.all(), attrs={"class": "form-control"}),
            'classification': forms.Select(choices=DeweyDecimalClassification.objects.all(), attrs={"class": "form-control"}),
            'publisher': forms.Select(choices=Publisher.objects.all(), attrs={"class": "form-control"}),
            'code': forms.TextInput(attrs={'placeholder': 'e.g. How to sleep', "class": "form-control"}),
            'pages_num': forms.NumberInput(attrs={'placeholder': '500', "class": "form-control"}),
            'available_copies': forms.NumberInput(attrs={'placeholder': '500', "class": "form-control"}),
            'date_published': forms.DateInput(attrs={"type": "date"}),
            'date_added': forms.DateInput(attrs={"type": "date"}),
            'available_borrowing': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'available': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'image': forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
            'brief': CKEditorWidget(),
        }


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'image', 'bio', 'birth_place', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Naguib Mahfouz', "class": "form-control", 'id': 'AuthorName'}),
            'image': forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
            'bio': CKEditorWidget(attrs={"label": "bio"}),
            'birth_place': forms.Select(choices=City.objects.all(), attrs={"class": "form-control"}),
        }


class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. El-Nahda', "class": "form-control", 'id': 'PublisherName'}),
        }


class CityCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. cairo', "class": "form-control", 'id': 'CityName'}),
        }
