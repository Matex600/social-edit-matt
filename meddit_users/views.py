from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from meddit_users.models import UserProfile
from .forms import (RegisterForm, EditUserForm,
                    PasswordUpdatingForm, ProfileForm)


# I have disabled error too many ancestors as I have have been unable to fix
# within time scale as it would mean re writing code this is will be a future update.


class CreateProfilePageView(CreateView):  # pylint: disable=too-many-ancestors
    """
    View using form profileform to for creating user profile.
    """
    model = UserProfile
    form_class = ProfileForm
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfileView(generic.UpdateView):  # pylint: disable=too-many-ancestors
    """
    View to displaying form in update profile template.
    """
    model = UserProfile
    form_class = ProfileForm
    template_name = 'registration/update_profile_page.html'
    success_url = reverse_lazy('home')


class UserProfilePageView(DetailView):
    """
    View for displaying users profile using primary keys [pk].
    """
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user_id = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['user_id'] = user_id
        return context


class UpdatePasswordsView(PasswordChangeView):  # pylint: disable=too-many-ancestors
    """
    View for custom form to display updating user password.
    """
    form_class = PasswordUpdatingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    """
    User returned to success page once they change password.
    """
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):  # pylint: disable=too-many-ancestors
    """
    View for registering users using customised form.
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):  # pylint: disable=too-many-ancestors
    """
    View for editing users profile using customised form.
    """
    form_class = EditUserForm
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user
