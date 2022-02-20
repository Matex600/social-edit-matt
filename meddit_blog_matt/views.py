from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category, Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm


class MainView(ListView):
    """
    View for index.html PLACEHOLDER
    """
    model = Post
    template_name = 'index.html'
    paginate_by = 10
    cate = Category.objects.all()
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context


class BlogDetailView(DetailView):
    """
    View for individual pages for each post
    """
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        likes_id = get_object_or_404(Post, id=self.kwargs['pk'])
        number_of_likes = likes_id.number_of_likes()

        liked = False
        if likes_id.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cate_menu'] = cate_menu
        context['number_of_likes'] = number_of_likes
        context['Liked'] = liked
        return context


def like_view(request, pk):
    """
    View for individual pages for each post PLACEHOLDER
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        

class AddPostView(LoginRequiredMixin, CreateView):
    """
    View for add_blog_post.html PLACEHOLDER
    """
    model = Post
    form_class = AddPostForm
    template_name = 'add_blog_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    """
    View for add_blog_post.html PLACEHOLDER
    """
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})


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


def handler400(request, exception):
    """
    Handler for Bad Request 400
    """
    return render(request, "400.html", status=400)


def handler403(request, exception):
    """
    Handler forbidden request 403
    """
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """
    Handler for not found request 404
    """
    return render(request, "404.html", status=404)


def handler500(request, *args, **argv):
    """
    Handler for internal server error generic message 500
    """
    return render(request, "500.html", status=500)

