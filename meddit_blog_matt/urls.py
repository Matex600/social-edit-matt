from django.urls import path
from .views import MainView, BlogDetailView, AddPostView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
