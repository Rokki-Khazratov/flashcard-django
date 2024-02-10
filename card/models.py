from django.db import models as m
from django.contrib.auth.models import User


# Create your models here.

class Category(m.Model):
    name = m.CharField(max_length=250)


    def __str__(self):
        return self.name


class Word(m.Model):
    name = m.CharField(max_length  = 250)
    translate_uz = m.CharField(max_length  = 250)
    translate_ru = m.CharField(max_length  = 250,blank=True)
    category = m.ForeignKey(Category, on_delete = m.CASCADE)

    def __str__(self):
        return self.name
    

class User(m.Model):
    user = m.OneToOneField(User,on_delete = m.DO_NOTHING)
    user_name = m.CharField(max_length=250)
    password = m.IntegerField(default=1)
    email = m.EmailField(blank=True)
    words = m.ManyToManyField(Word,related_name='words')
    in_correct_words = m.ManyToManyField(Word,related_name='incorrect_words')


    def __str__(self):
        return self.user_name
