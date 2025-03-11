from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now=True)
    author = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipes', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredient'
    )

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}: x{self.quantity}'