from django.urls import path
from django.contrib import admin
from algobourso import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user/' , views.user, name='user'),
    path ('performance/' , views.performance, name='performance'),
    path ('portefeuille/' , views.portefeuille, name='portefeuille'),
    path ('strategies/' , views.strategies, name='strategies'),
    path ('forum/' , views.forum, name='forum'),
    path ('actions/' , views.actions, name='actions'),
]



