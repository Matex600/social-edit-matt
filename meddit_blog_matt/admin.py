from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class BlogAdmin(SummernoteModelAdmin):
    """
    Class that populates fields when creating a post in the Django Admin Panel
    """
    list_display = ('title', 'author', 'updated_on', 'status', 'date_created')
    search_fields = ['title', 'body']
    list_filter = ('status', 'date_created')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class that populates fields when creating a comment in the Django Admin Panel
    """
    list_display = ('name', 'content', 'post', 'date_created', 'approved')
    list_filter = ('approved', 'date_created')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function for approving comments by an Administrator
        """
        queryset.updated(approved=True)


admin.site.register(Category)