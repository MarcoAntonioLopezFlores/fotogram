from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'',include(('posts.urls','posts'),namespace='posts')),
    path('admin/', admin.site.urls),
    path('users/',include(('users.urls','users'),namespace='users'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
