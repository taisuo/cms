from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist/', views.regist),
    path('login/', views.login),
    path('registHangle/',views.registHangle)
 ]