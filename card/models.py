from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class User(models.Model):
    user_name = models.CharField(max_length=250)
    password = models.IntegerField(default=1)
    email = models.EmailField
    words = models.ManyToManyField
    in_correct_words = models.ManyToManyField


    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length  = 250)
    translate_uz = models.TextField
    translate_ru = models.TextField
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    


