from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView, add_image

urlpatterns = [
    path("recipes", RecipeListView.as_view(), name="recipes"),
    path("recipe/<int:pk>", RecipeDetailView.as_view(), name="recipe"),
    path("recipe/add", RecipeCreateView.as_view(), name="add-recipe"),
    path("recipe/<int:pk>/add_image", add_image, name="add-image"),
]

app_name = "ledger"
