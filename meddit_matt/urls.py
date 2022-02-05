from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meddit_blog_matt.urls')),
    path('summernote/', include('django_summernote.urls'))
]
