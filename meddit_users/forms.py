from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       PasswordChangeForm)
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """
    Form class for profile.
    """
    class Meta:
        """
        Meta class adds widgets to determine inputs and style classes.
        """
        model = UserProfile
        fields = ('user_bio', 'user_image', 'github_url', 'linkedin_url',
                  'facebook_url', 'twitter_url', 'instagram_url')
        widgets = {
            'user_bio': forms.Textarea(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    """
    Form for displaying fields when user registers.
    """
    email = forms.EmailField(widget=forms.
                             EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        """
        Meta class to display fields for registering a user to the blog page.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Function to style user registering fields.
        """
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class EditUserForm(UserChangeForm):
    """
    Form used to style fields for editing a user profile.
    """
    email = forms.EmailField(widget=forms.
                             EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.
                                 TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.
                                TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
                               widget=forms.
                               TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(disabled=True,
                                 widget=forms.
                                 TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(disabled=True,
                                  widget=forms.
                                  TextInput(attrs={'class': 'form-control'}))
    is_superuser = None
    is_staff = None
    is_active = None
    email = None

    class Meta:
        """
        Meta class displaying fields for editing user profile.
        """
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'date_joined', 'last_login')


class PasswordUpdatingForm(PasswordChangeForm):
    """
    Form used to style fields for password updating.
    """
    old_password = forms.CharField(label='Old Password',
                                   widget=forms.PasswordInput
                                   (attrs={'class': 'form-control',
                                           'type': 'password'}))
    new_password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                            'type': 'password'}))
    new_password2 = forms.CharField(label='Confirm Password',
                                    widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                            'type': 'password'}))

    class Meta:
        """
        Meta class displays fields when updating password.
        """
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
