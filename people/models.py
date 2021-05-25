from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Person(models.Model):
    name = CharField(max_length=50)
    age = IntegerField()
    occupation = CharField(max_length=50)