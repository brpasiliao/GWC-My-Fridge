from django.shortcuts import render
from .models import Recipe
from django.shortcuts import render, get_object_or_404
from .forms import RecipeForm
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
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'fridge/recipe_edit.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'fridge/recipe_edit.html', {'form': form})
