from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloAPI),
    path('<str:id_user>/', views.todoMamangerUser),
    path('', views.index),
]