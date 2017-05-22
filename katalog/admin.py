from django.contrib import admin
from .models import Author, Book, Publisher, Item


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author__last_name')


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    inlines = (BookInline, )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(
    [Publisher, Item]
    )

