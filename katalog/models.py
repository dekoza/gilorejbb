from django.db import models

class Author(models.Model):
    "Autor"
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name,
                                                 last_name=self.last_name)

class Book(models.Model):
    "Ksiażka"   # napis dokumentujacy (dokumentacja)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    
    def __str__(self):
        return self.title

class Publisher(models.Model):
    "Wydawnictwo"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    "Egzemplarz"
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher)
    year = models.IntegerField()
    
    def __str__(self):
        return "{book} ({year} - {publisher})".format(book=self.book.title,
                                                      year=self.year,
                                                      publisher=self.publisher)
