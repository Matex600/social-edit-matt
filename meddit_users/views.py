from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from meddit_users.models import UserProfile
from .forms import RegisterForm, EditUserForm, PasswordUpdatingForm

class UpdateProfileView(generic.UpdateView):
    """
    View to display edit profile page template
    """
    model = UserProfile
    template_name = 'registration/update_profile_page.html'
    fields = ['user_bio', 'user_image', 'github_url', 'linkedin_url', 'facebook_url', 'twitter_url', 'instagram_url']
    success_url = reverse_lazy('home')



class UserProfilePageView(DetailView):
    """
    View for displaying user profile page
    """
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user_id = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['user_id'] = user_id
        return context


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