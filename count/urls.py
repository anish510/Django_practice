from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second_index/', views.second_index, name='second_index'),
    path('counter', views.counter, name='counter'),

]
