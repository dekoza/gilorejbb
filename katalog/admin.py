from django.contrib import admin
from .models import Author, Book, Publisher, Item

admin.site.register(
    [Author, Book, Publisher, Item]
    )

