from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class BlogAdmin(SummernoteModelAdmin):
    """
    Class for creating blog post in admin view
    """
    list_display = ('title', 'author', 'updated_on', 'slug', 'status', 'date_created')
    search_fields = ['title', 'body']
    list_filter = ('status', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class for creating comments in admin view
    """
    list_display = ('name', 'content', 'post', 'date_created', 'approved')
    list_filter = ('approved', 'date_created')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.updated(approved=True)

admin.site.register(Category)