from django.urls import path

from .views import index, recipes, recipe

urlpatterns = [
    path("", index, name="index"),
    path("recipes", recipes, name="recipes"),
    path("recipe/<int:recipe_no>", recipe, name="recipe")
]

app_name = "ledger"
