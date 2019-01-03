from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SeasonalIngredients
# Create your views here.

def index(result) :
    return HttpResponse("index.html")

class ListIngredientsView(ListView) :

    model = SeasonalIngredients
    template_name = 'seasonal_ingredient.html'