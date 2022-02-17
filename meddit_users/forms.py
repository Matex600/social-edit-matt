from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    """
    Form used to style fields for registering a user to the blog page
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """
        Display fields for registering user
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Function to style user registering fields
        """
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditUserForm(UserChangeForm):
    """
    Form used to display fields for editing a user profile
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = None
    is_staff = None
    is_active = None
    email = None

    class Meta:
        """
        Display fields for editing user profile
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_joined', 'last_login')


class PasswordUpdatingForm(PasswordChangeForm):
    """
    Form used to style fields for registering a user to the blog page
    """
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        """
        Display fields for registering user
        """
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')