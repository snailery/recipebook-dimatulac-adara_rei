from django.contrib import admin
from .models import Recipe

class RecipeInline(admin.TabularInline):
    model = Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)

    fieldsets = [
        ('Details', {
            'fields': [
                ('name')
            ]
        }),
    ]

admin.site.register(Recipe, RecipeAdmin)