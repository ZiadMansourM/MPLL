from django import forms
from .models import Comment, Post, Reply, ContactUs
from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields =['title', 'is_pinned', 'content', 'image']

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
            'email',
            'telephone',
            'message',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'telephone': forms.NumberInput(attrs={'placeholder': 'Telephone'}),
            'message': forms.Textarea(attrs={'rows': '5'})
        }
