from django.contrib import admin
from .models import (Diet, Ingredient, Meal, Recipe, Session, Ustensil,
                     MealParticipant, RecipeIngredient, ParentRecipe)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class MealParticipantInline(admin.TabularInline):
    model = MealParticipant


class SessionMealInline(admin.TabularInline):
    model = Meal


class ParentRecipeInline(admin.TabularInline):
    model = ParentRecipe
    fk_name = 'child'
    extra = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'diets_str')
    exclude = ['diets']
    list_filter = ('diets__name',)
    search_fields = ['name', 'diets__name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'diets_str', 'price', 'meal_type', 'parts')
    exclude = ['diets']
    inlines = [RecipeIngredientInline, ParentRecipeInline]
    list_filter = ('diets__name', 'meal_type')
    search_fields = ['name', 'meal_type', 'diets__name', 'description']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    filter_horizontal = ('recipes',)
    inlines = [MealParticipantInline, ]
    list_display = ('name', 'participants_count', 'date',
                    'admin_roadmap')
    search_fields = ['name', 'recipes__name']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_roadmap')
    inlines = [SessionMealInline]


admin.site.register(Diet)
admin.site.register(Ustensil)
# admin.site.register(MealParticipant)
# admin.site.register(RecipeIngredient)
