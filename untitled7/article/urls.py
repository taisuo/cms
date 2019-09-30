from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
    path('addArticle/', views.addArticle),
    path('getArticleList/', views.getArticleList),
    path('articleDite/', views.articleDite),
    path('getusername/', views.getusername),
    path('addArticleHangle/', views.addArticleHangle),
    path('getarticleDiteinfo/', views.getarticleDiteinfo),
]