from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main import settings
from .views import *


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('catalogue/', catalogue, name='catalogue'),
    path('catalogue2/', catalogue2, name='catalogue2'),
    path('login/', include ('django.contrib.auth.urls')),
    path('annonce', annonce, name='annonce'),
    path('annonce/update/<int:pk>', update_annonce, name='modifier_annonce'),
    path('annonce/delete/<int:pk>', delete_annonce, name='delete'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
