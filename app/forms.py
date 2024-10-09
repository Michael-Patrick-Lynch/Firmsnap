from django import forms
from .models import Post, Comment


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_text"]


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]

# For use by org admins
class BulkUserAddForm(forms.Form):
    user_data = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter users as "username, password" one per line'}),
        help_text="Add users in the format: username, password"
    )