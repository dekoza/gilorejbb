from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    # przygotowanie danych do wyświetlenia!

    kontekst = {
        "title": "Hejka hejka",
        "liczba": 42,
        "napis": "Ala Makota",
        "lista": ["chleb", "maslo", "śmietana 10%", "mleko", "jaja", "warzywa"]
        }

    return render(request, "katalog/index.html", context=kontekst)
