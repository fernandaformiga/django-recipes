from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipeslist(request):
    recipes = Recipe.objects.all()

    data = {
        'recipes': recipes
    }
    return render(request,'recipeslist.html', data)