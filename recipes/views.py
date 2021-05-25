from django.shortcuts import get_object_or_404, render
from .models import Recipe

# Create your views here.
def recipeslist(request):
    recipes = Recipe.objects.all()

    data = {
        'recipes': recipes
    }

    return render(request,'recipeslist.html', data)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    displayed_recipe = {
        'recipe': recipe
    }

    return render(request, 'recipe.html', displayed_recipe)