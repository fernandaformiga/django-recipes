from django.contrib import admin
from .models import Person

class PeopleList(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# Register your models here.
admin.site.register(Person, PeopleList)