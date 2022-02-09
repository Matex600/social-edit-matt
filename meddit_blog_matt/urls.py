from django.urls import path
from .views import MainView, BlogDetailView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
]
