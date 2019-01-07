from django.shortcuts import render
from .models import SeasonalIngredients
from .forms import selectForm
from datetime import datetime

# Create your views here.
app_name = 'eatwhat'

def main_page(request) :
    print("posting")
    month = request.GET.get('month', datetime.today().month)
    form = selectForm({'month' : month})
    food_list = SeasonalIngredients.objects.filter(month=month)

    return render(request, 'eatwhat/main_page.html',{'form' : form, 'month' : month, 'food_list' : food_list})

