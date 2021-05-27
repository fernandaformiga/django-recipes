from django.db import models
from people.models import Person

# Create your models here.
class Recipe(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField()
    prep = models.TextField()
    prep_time = models.IntegerField()
    category =  models.CharField(max_length=100)