from django import forms 
from .models import Comment, Post
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
