from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class AddPostForm(forms.ModelForm):
    """
    Class that uses bootstrap classes to style fields
    Populates fields when creating post
    """
    class Meta:
        """
        Form class for my create post functionality PLACEHOLDER
        """
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'post_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a blog title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """
    Class that uses bootstrap classes to style fields
    Populates fields when editing fields
    """
    class Meta:
        """
        Form class for my create post functionality PLACEHOLDER
        """
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
