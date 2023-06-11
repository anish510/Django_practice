from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second_index/', views.second_index, name='second_index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),


]
