from django.contrib import admin
from .models import Category, Word ,User

admin.site.register(Word)
admin.site.register(User)

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name','id']


# @admin.register(Word)
# class Word(admin.ModelAdmin):
#     list_display = ['name', 'translate_uz' , 'translate_ru']
