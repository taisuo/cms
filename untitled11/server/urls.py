from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('content', views.content),
    path('contentHandle', views.contentHandle),
    path('selectcontentHandle', views.selectcontentHandle),
    path('contentlist', views.contentlist),
    path('addcontentlist', views.addcontentlist),
    path('addcontent', views.addcontent),
    path('delcontentHandle', views.delcontentHandle),
    path('btnclickaddHandle', views.btnclickaddHandle),
    path('menu', views.menu),
    path('menuHandle', views.menuHandle),
    path('menulist', views.menulist),
    path('recommend', views.recommend),
    path('recommendHandle', views.recommendHandle),
    path('recommendlist', views.recommendlist),
    path('delrecommendHandle', views.delrecommendHandle),
    path('addrecommendlist', views.addrecommendlist),
    path('addrecommendlistHandle', views.addrecommendlistHandle),
    path('admin', views.admin),
    path('adminHandle', views.adminHandle),
    path('adminlist', views.adminlist),
    path('deladminHandle', views.deladminHandle),
    path('login', views.login),
    path('loginHandle', views.loginHandle),
    path('delHandle', views.delHandle),
    path('indexHandle', views.indexHandle),
]