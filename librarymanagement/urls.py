"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Books.views import books_create_view, list_all, register, books_update_view, books_delete_view, books_detail_view


urlpatterns = [
    path("", list_all, name="homepage"),
    path('admin/', admin.site.urls, name="admin"),
    path('create/', books_create_view, name="create"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name="register"),
    path('detail/<int:id>/', books_detail_view, name="detail"),
    path("detail/<int:id>/delete", books_delete_view, name="delete"),
    path("create/<int:id>/update", books_update_view, name="update"),

]
