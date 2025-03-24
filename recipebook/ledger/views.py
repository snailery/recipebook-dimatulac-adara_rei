# from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = RecipeForm
    
    def get_success_url(self):
        return reverse('ledger:recipes')


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse('ledger:recipes')


def add_image(request, pk):
    form = RecipeImageForm()

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('ledger:recipe', args=[pk]))
        else:
            form = RecipeImageForm()
            
    ctx = {
        'form': form,
        'pk': pk
    }

    return render(request, 'add_image.html', ctx)
