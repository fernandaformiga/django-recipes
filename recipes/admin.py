from django.contrib import admin
from .models import Recipe

class RecipesList(admin.ModelAdmin):
    list_display = ('id', 'recipe_name')
    list_display_links = ('id',)
    search_fields = ('nome_receita',)
    search_fields = ('category',)

# Register your models here.
admin.site.register(Recipe, RecipesList)