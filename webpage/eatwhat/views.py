from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import SeasonalIngredients
from .forms import selectForm

# Create your views here.
app_name = 'eatwhat'

def main_page(request, month=12, food_list = []) :
    print("posting")
    form = selectForm(request.GET)

    month = request.GET.get('month',12)
    print("this is month %d" %month)


    food_list = SeasonalIngredients.objects.filter(month=month)


    return render(request, 'eatwhat/main_page.html',{'form' : form, 'month' : month, 'food_list' : food_list})

