from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:movie_id>/', detail, name="detail"),
    path('create/', create, name="create"),
    path('edit/<str:movie_id>/', edit, name = "edit"),
    path('update/<str:movie_id>/', update, name ="update"),
    path('delete/<str:movie_id>/', delete, name = 'delete'),

]
