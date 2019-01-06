from django.http import HttpResponse
from django.shortcuts import render
from .models import SeasonalIngredients


# Create your views here.

def main_page(request, month=12) :
    food_list = SeasonalIngredients.objects.filter(month = month)
    context = {
        'food_list' : food_list,
    }

    return render(request, 'eatwhat/main_page.html', context)
    ##form = selectForm()
    ##return HttpResponse("main_page.html", {'form' : form})

"""
    model = SeasonalIngredients
    template_name = 'main_page.html'
    
    <form method = "POST" class ='main_page'>
    {% csrf_token%}
    {{form.as_p}}
</form>
"""