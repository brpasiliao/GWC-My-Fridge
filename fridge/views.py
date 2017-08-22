from .models import Recipe
from .models import Food
from .forms import RecipeForm
from .forms import FoodForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.order_by('title')
    return render(request, 'fridge/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'fridge/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe_form = RecipeForm()
    return render(request, 'fridge/recipe_new.html', {'recipe_form': recipe_form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        if 'delete' in request.POST:
            recipe.delete()
            return redirect('recipe_list')
        else:
            recipe_form = RecipeForm(request.POST, instance=recipe)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(request, 'fridge/recipe_edit.html', {'recipe_form': recipe_form})

def my_fridge(request):
    food = Food.objects.order_by('name')

    if request.method == "POST":
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit=False)
            food.save()
            return redirect('my_fridge')
    else:
        food_form = FoodForm()
    return render(request, 'fridge/my_fridge.html', {'food_form': food_form, 'food': food})
