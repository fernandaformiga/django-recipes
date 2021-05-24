from django.urls import path

from . import views

urlpatterns = [
    path('recipeslist', views.recipeslist, name='recipeslist')
]