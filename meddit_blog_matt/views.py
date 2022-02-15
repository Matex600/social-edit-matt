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
    paginate_by = 6
    cate = Category.objects.all()
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context


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


def category_list_view(request):
    """
    View for add_blog_post.html PLACEHOLDER
    """
    cate_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cate_menu_list': cate_menu_list})


def category_view(request, cate):
    """
    View for add_blog_post.html PLACEHOLDER
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
