from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acticleList/', views.acticleList),
    path('addActicle/', views.addActicle),
    path('acticleListHandle/', views.acticleListHandle),
    path('addActicleHandle/', views.addActicleHandle),
    path('list/', views.list),
    path('listyer/', views.listyer),
]