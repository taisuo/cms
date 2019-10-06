from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('content', views.content),
    path('contentHandle', views.contentHandle),
    path('contentlist', views.contentlist),
    path('menu', views.menu),
    path('menuHandle', views.menuHandle),
    path('menulist', views.menulist),
    path('recommend', views.recommend),
    path('recommendHandle', views.recommendHandle),
    path('admin', views.admin),
    path('adminHandle', views.menulist),
    path('login', views.login),
    path('loginHandle', views.loginHandle),

]