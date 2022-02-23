from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meddit_blog_matt.urls'), name='meddit_blog_matt.urls'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('meddit_users.urls'), name='meddit_users'),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
