from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditUserForm


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