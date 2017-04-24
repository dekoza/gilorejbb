from django.db import models

class Author(models.Model):
    "Autor"
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Book(models.Model):
    "Ksiażka"   # napis dokumentujacy (dokumentacja)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    

class Publisher(models.Model):
    "Wydawnictwo"
    name = models.CharField(max_length=100)


class Item(models.Model):
    "Egzemplarz"
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher)
    year = models.IntegerField()
    