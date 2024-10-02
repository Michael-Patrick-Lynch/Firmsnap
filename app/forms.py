from django import forms
from .models import Post, Comment

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text']

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
