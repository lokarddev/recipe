from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *


class HomeView(View):
    """The main page of the site. Contains the latest 4 recipes as table of cards"""
    def get(self, request):
        context = {
            'topics': Topic.objects.all()[:3],
            'recipes': Recipe.objects.all()[:3]
        }
        return render(request, template_name='main_recipe/home.html', context=context)


class CategoryView(View):
    """Category page with a table of cards ordered by their category. Every card is a link contains a list of recipes"""
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, template_name='main_recipe/category.html', context=context)


class GetData:
    """Класс для обработки запросов к дате"""
    def get_ingredient(self):
        return Ingredient.objects.all()


class ConstructorView(GetData, ListView):
    """The main feature of the site. Basically works as simple filter page at e-commerce. Contains table of categories
    and list of products to choose from"""
    model = Recipe
    template_name = 'main_recipe/constructor.html'
    queryset = Recipe.objects.filter(draft=False)


class FilterView(GetData, ListView):
    """Фильтр который отображается на странице Constructor.html
        Показвыает выборку на основе отмеченных ингредиентов."""
    def get_queryset(self):
        queryset = Recipe.objects.filter(
            ingredient__in=self.request.GET.getlist('ingredient')
        ).distinct()
        return queryset


class TopicDetail(View):
    """Detailed description page of the chosen TOPIC"""
    def get(self, request, pk):
        context = {
            'topic': Topic.objects.get(id=pk),
        }
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class RecipeDetail(View):
    """Detailed description page of the chosen RECIPE"""
    def get(self, request, pk):
        context = {
            'recipe': Recipe.objects.get(id=pk),
        }
        return render(request, template_name='main_recipe/recipe_detail.html', context=context)


class CategoryList(View):
    """List of recipes from concrete chosen CATEGORY"""
    def get(self, request, pk):
        context = {
            'recipes': Recipe.objects.filter(category__id=pk)
        }
        return render(request, template_name='main_recipe/category_list.html', context=context)


class TopicList(View):
    """Полный список статей на сайте"""
    def get(self, request):
        context = {
            'topics': Topic.objects.order_by('-created')
        }
        return render(request, template_name='main_recipe/topic_list.html', context=context)


class RecipeList(GetData, ListView):
    """Полный список рецептов на сайте"""
    model = Recipe
    queryset = Recipe.objects.order_by('-created')
