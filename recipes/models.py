from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField()
    prep = models.TextField()
    prep_time = models.IntegerField()
    category =  models.CharField(max_length=100)