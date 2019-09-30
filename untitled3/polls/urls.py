from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register),
    path('login', views.login),
    path('list', views.list),
    path('add', views.add),
]
