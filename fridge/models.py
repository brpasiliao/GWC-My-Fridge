from django.db import models
# from django.utils import timezone


class Recipe(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title

class Food(models.Model):
    name = models.CharField(max_length=200)
    default_food_type = "Type"
    food_type_choices = (
        (default_food_type, "Type"),
        ("DAIRY", "Dairy"),
        ("MEAT", "Meat"),
        ("VEGETABLE", "Vegetable")
    )
    food_type = models.CharField(max_length=200, choices=food_type_choices, default=default_food_type)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
