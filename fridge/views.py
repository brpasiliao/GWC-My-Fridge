from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.order_by('title')
    return render(request, 'fridge/recipe_list.html', {'recipes': recipes})
