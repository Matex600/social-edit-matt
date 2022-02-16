from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditUserForm, PasswordUpdatingForm


class UpdatePasswordsView(PasswordChangeView):
    """
    View for changing style when updating password
    """
    form_class = PasswordUpdatingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    """
    User taken to page once password is changed successfully
    """
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    """
    View for registering users using django forms
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):
    """
    View for registering users using django forms
    """
    form_class = EditUserForm
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user