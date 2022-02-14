from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import AddPostForm, EditPostForm


class MainView(ListView):
    """
    View for index.html PLACEHOLDER
    """
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    paginate_by = 6
    ordering = ['-date_created']


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


def category_view(request, cate):
    """

    """
    category_posts = Post.objects.filter(category=cate.replace('-', ' '))
    return render(request, 'categories.html', {'cate': cate.title().replace('-', ' '), 'category_posts': category_posts})


class AddCategoryView(CreateView):
    """
    View for add_blog_post.html PLACEHOLDER
    """
    model = Category  
    template_name = 'add_category.html'
    fields = '__all__'


class EditPostView(UpdateView):
    """
    View for edit_blog_post.html PLACEHOLDER
    """
    model = Post
    form_class = EditPostForm
    template_name = 'edit_blog_post.html'


class DeletePostView(DeleteView):
    """
    View for delete_blog_post.html PLACEHOLDER
    """
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('home')
