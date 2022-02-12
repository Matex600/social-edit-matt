from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    """
    View for registering users using django forms
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
