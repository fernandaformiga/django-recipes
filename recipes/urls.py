from django.urls import path

from . import views

urlpatterns = [
    path('recipeslist', views.recipeslist, name='recipeslist'),
    path('<int:recipe_id>', views.recipe, name='recipe'),
]