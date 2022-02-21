from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('login_app.urls')),
    path('', include('blog_app.urls')),
 
       
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)