from django import forms
from .models import Post, Category, Comment


class AddPostForm(forms.ModelForm):
    """
    Form for adding blog posts.
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        Populate fields when creating a post.
        """
        model = Post
        fields = ('title', 'category', 'body', 'blog_snippet',
                  'post_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Choose a blog title!'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """
    Form for editing blog posts.
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        populate fields when editing fields in a post.
        """
        model = Post
        fields = ('title', 'category', 'body', 'blog_snippet', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddCommentForm(forms.ModelForm):
    """
    Form for adding comments for blog posts.
    """
    class Meta:
        """
        Class that uses bootstrap classes to style comment field
        and populate fields when editing comments.
        """
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
