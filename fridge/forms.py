from django import forms
from .models import Recipe
from .models import Food

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions',)

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'food_type', 'expiration_date',)

# class DeleteFoodForm()
