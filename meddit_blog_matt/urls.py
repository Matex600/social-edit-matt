from django.urls import path
from .views import MainView, BlogDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
