from django.contrib import admin
from .models import Category, Word 
#,User
# Register your models here.
admin.site.register(Category)
admin.site.register(Word)
#admin.site.register(User)

# @admin.register(Category)
# class Category(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(Word)
# class Word(admin.ModelAdmin):
#     list_display = ['name', 'translate_uz' , 'translate_ru']
