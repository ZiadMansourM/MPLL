from django import forms 
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields =['title', 'content', 'image']
