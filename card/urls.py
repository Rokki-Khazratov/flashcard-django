from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name='index'),
    path('all_category/', all_category, name='all_category'),
    path('category_detail/<int:category_id>/', category_detail , name='category_detail'),
    path('word_detail/<int:word_id>/', word_detail , name = 'word_detail'),


    path('register/', register, name='register'),
    path('login/', login, name='login'),


    # path('learn/', learn, name='learn'),
    # path('known/', known, name='known'),
    # path('unknown/', unknown, name='unknown'),
]