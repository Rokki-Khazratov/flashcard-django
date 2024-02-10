from django.shortcuts import render
from .models import *
# Create your views here.

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


#contextda hato ,html bilan solishtir
def category_detail(request , category_id ):
    details = Category.objects.filter( id = category_id)
    context = {
        'details' : details ,    
    }


    return render(request , 'category_detail.html' , context )



#views notogri emas,htmlni yoz
def word_detail(request, word_id):
    words = Word.objects.filter( id = word_id )
    translate_uz = Word.objects.all()
    context = {
        'words' : words ,
        'translate_uz' : translate_uz,
    }

    return render(request, 'word_detail.html', context )
