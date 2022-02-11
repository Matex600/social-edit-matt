from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    """
    Form class for my create post functionality PLACEHOLDER
    """
    class Meta:
        """
        Form class for my create post functionality PLACEHOLDER
        """
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'post_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a blog title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """
    Form class for my create post functionality PLACEHOLDER
    """
    class Meta:
        """
        Form class for my create post functionality PLACEHOLDER
        """
        model = Post
        fields = ('title', 'title_tag', 'body', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
