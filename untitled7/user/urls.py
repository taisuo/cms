from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist/', views.regist),
    path('login/', views.login),
    path('registHangle/', views.registHangle),
    path('loginHangle/', views.loginHangle),
]
