from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class MainView(ListView):
    """
    View for index.html PLACEHOLDER
    """
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    paginate_by = 4


class BlogDetailView(DetailView):
    """
    View for individual pages for each post
    """
    model = Post
    template_name = 'blog_details.html'