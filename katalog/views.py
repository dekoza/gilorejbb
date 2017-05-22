from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Book

# Create your views here.


class TestForm(forms.Form):
    nazwisko = forms.CharField()
    

 



def index(request):
    
    # przygotowanie danych do wyświetlenia!

    if request.method == "POST":
        
        nazwisko = request.POST.get('nazwisko')
        rezultat = Book.objects.filter(
            author__last_name__startswith=nazwisko
            )
        
        
        kontekst = {
            "show_form": False,
            "wyniki": rezultat,
            }

    else:
        kontekst = {
            "show_form": True,
            }


    return render(request, "katalog/index.html", context=kontekst)
