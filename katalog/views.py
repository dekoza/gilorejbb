from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.generic import ListView, DetailView

from .models import Book, Author

# Create your views here.

def index(request):
    # widok jako funkcja (staro
    # przygotowanie danych do wyświetlenia!
#     if request.method == "POST":
#         nazwisko = request.POST.get('nazwisko')
#         rezultat = Book.objects.filter(
#             author__last_name__startswith=nazwisko
#             )
#         kontekst = {
#             "show_form": False,
#             "wyniki": rezultat,
#             }
#     else:
#         kontekst = {
#             "show_form": True,
#             }
    return render(request, "katalog/index.html") #, context=kontekst)

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author
