from .models import *
from .models import User as carduser
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate

def index(request):
    categories= Category.objects.all()

    context = {
        'categories' : categories,
    }    
    return render(request,'index.html', context)


def all_category(request):
    categories = Category.objects.all()

    context = {
        'categories' : categories ,
    }

    return render(request, 'all_category.html' , context )



def category_detail(request , category_id ):
    details = Category.objects.get( id = category_id)
    dictionary = Word.objects.filter( category_id = category_id )
    context = {
        'details' : details ,
        'dictionary' : dictionary

    }


    return render(request , 'category_detail.html' , context )


def word_detail(request, word_id):
    words = Word.objects.filter( id = word_id )
    translate_uz = Word.objects.all()
    context = {
        'words' : words ,
        'translate_uz' : translate_uz,
    }

    return render(request, 'word_detail.html', context )




#?? --------------------user regoster 
#! 1. yaratilgan django-userni malumuotlarini olib regsiterdan keyin shunga teng app user yaratish
#? qila olmadim


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data[username]
            password = form.cleaned_data[password] 
            # django_user = User.objects.create_user(username = username, password = password)
            # form.save(django_user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

