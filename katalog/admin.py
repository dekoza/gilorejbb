from django.contrib import admin
from .models import Author, Book, Publisher, Item
from django.contrib.admin.templatetags.admin_list import date_hierarchy


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author__last_name')
    list_display = ('title', 'author')


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    inlines = (BookInline, )


class ItemInline(admin.TabularInline):
    model = Item
    

class ItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'publisher', 'pub_date')
    list_filter = ('pub_date', )
    date_hierarchy = 'pub_date'
    
class PublisherAdmin(admin.ModelAdmin):
    inlines = (ItemInline, )
    



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Item, ItemAdmin)

