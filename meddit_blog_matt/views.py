from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import AddPostForm


class MainView(ListView):
    """
    View for index.html PLACEHOLDER
    """
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    paginate_by = 6


class BlogDetailView(DetailView):
    """
    View for individual pages for each post
    """
    model = Post
    template_name = 'blog_details.html'

class AddPostView(CreateView):
    """
    View for add_blog_post.html PLACEHOLDER
    """
    model = Post
    form_class = AddPostForm
    template_name = 'add_blog_post.html'
    
