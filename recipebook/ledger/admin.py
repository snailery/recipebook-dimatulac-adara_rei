from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author', 'created_on', 'updated_on')
    list_display = ('name', 'author', 'created_on', 'updated_on')

    inlines = [RecipeIngredientInline]

    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'author'), 
            ]
        }),
    ]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)