"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from albums import views as albums_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', albums_views.list_albums, name='list_albums'),
    path('albums/add/', albums_views.add_album, name='add_album'),
    path('albums/<int:pk>/edit/',
         albums_views.edit_album,
         name='edit_album'),
    path('albums/<int:pk>/delete/',
         albums_views.delete_album,
         name='delete_album'),
    path('albums/<int:pk>/album/', albums_views.add_album, name='add_album'),
    path('albums/<int:pk>/', albums_views.album_detail, name='album_detail'),
]
