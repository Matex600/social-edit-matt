from django.urls import path
from .views import (MainView, BlogDetailView, AddPostView, EditPostView,
                    DeletePostView, AddCategoryView, category_view,
                    category_list_view, like_view,
                    AddCommentView, results_view)

# Handler path to handler views
HANDLER400 = 'meddit_blog_matt.views.handler400'
HANDLER403 = 'meddit_blog_matt.views.handler403'
HANDLER404 = 'meddit_blog_matt.views.handler404'
HANDLER500 = 'meddit_blog_matt.views.handler500'


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cate>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),
    path('like/<int:pk>', like_view, name='up_vote_post'),
    path('blog/<int:pk>/comment/',
         AddCommentView.as_view(), name='add_comment'),
    path('search_results', results_view, name='search_results'),
]
