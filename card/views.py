from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    
    return render(request,'index.html')


def all_category(request):
    name = Category.objects.all()
    context = {
        'name' : name ,
    }

    return render(request, 'all_category.html' , context )



def category_detail(request , category_id ):
    names = Category.objects.filter( id = category_id)
    context = {
        'name' : names ,    
    }


    return render(request , 'category_detail.html' , context )



def word_detail(request, word_id):
    name = Word.objects.filter( id = word_id )
    translate_uz = Word.objects.all()
    translate_ru = Word.objects.all()
    context = {
        'name' : name ,
        'translate_uz' : translate_uz,
        'translate_ru' : translate_ru
    }

    return render(request, 'word_detail.html', context )
