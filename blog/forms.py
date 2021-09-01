from django import forms
from .models import Comment, Post, Reply, ContactUs, Category
from ckeditor.widgets import CKEditorWidget


class FilterSearchBlogHome(forms.ModelForm):
    class Meta:
        model = Post
        fields =['categories', "is_pinned"]
        widgets = {
            'categories': forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%"
                },
            ),
            'is_pinned': forms.CheckboxInput(attrs={"class": "customized-form-check-input"}),
        }

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields =['title', 'categories', 'is_pinned', 'content', 'image']
        widgets = {
            'categories': forms.SelectMultiple(attrs={"class": "form-control"}),
            'image': forms.ClearableFileInput(attrs={"class": "form-control form-control-sm clearablefileinput"}),
        }

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['comment']

class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields =['reply']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'is_urgent',
            'message',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'e.g. Ziad', "class": "form-control"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'e.g. Masnour', "class": "form-control"}),
            'username': forms.TextInput(attrs={'placeholder': 'username', "class": "form-control"}),
            'email': forms.EmailInput(attrs={'placeholder': 'ziad@devopsgeek.xyz', "class": "form-control"}),
            'is_urgent': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'message': forms.Textarea(attrs={"class": "form-control"})
        }
        labels = {
            'is_urgent': 'Urgent',
        }
