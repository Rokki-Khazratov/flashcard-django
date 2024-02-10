
from .models import *
from .models import User as carduser

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


#! details = shu {category_id} ga teng boganlari chiqishi kere
def category_detail(request , category_id ):
    details = Category.objects.filter( id = category_id)
    context = {
        'details' : details ,    
    }


    return render(request , 'category_detail.html' , context )



#! shu sozni hamma fieldlarini chiqarosh ( name, tarjimasi, qaysi category,)  misol=[eng_soz: car,uz_tarjima"moshina", category = p22]
def word_detail(request, word_id):
    words = Word.objects.filter( id = word_id )
    translate_uz = Word.objects.all()
    context = {
        'words' : words ,
        'translate_uz' : translate_uz,
    }

    return render(request, 'word_detail.html', context )




#?? --------------------user regoster 
#1. yaratilgan django-userni malumuotlarini olib regsiterdan keyin shunga teng app user yaratih
#2.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # carduser.objects.create(
            #     username=form.cleaned_data['username'],
            #     email=form.cleaned_data['email'],
            #     password=form.cleaned_data['password1']
            # )
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#login uchun  template yozasan
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

