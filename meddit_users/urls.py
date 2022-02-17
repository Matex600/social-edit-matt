from django.urls import path
from .views import UserRegisterView, UserUpdateView, UpdatePasswordsView, UserProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
    path('password/', UpdatePasswordsView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile', UserProfilePageView.as_view(), name='show_profile'),
]
