
from django.contrib import admin
from django.urls import  path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('memebers/', include('django.contrib.auth.urls')), # its give the user login and password form the django
    path('memebers/', include('memebers.urls')),

    # djanog 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)