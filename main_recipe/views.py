from django.shortcuts import render
from django.views import View
from .models import *
from django.core.exceptions import ObjectDoesNotExist


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


class ConstructorView(View):
    """The main feature of the site. Basically works as simple filter page at e-commerce. Contains table of categories
    and list of products to choose from"""
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/constructor.html', context=context)


class TopicDetail(View):
    """Detailed description page of the choosen TOPIC"""
    def get(self, request, pk):
        context = {
            'topic': Topic.objects.get(id=pk),
        }
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class RecipeDetail(View):
    """Detailed description page of the choosen RECIPE"""
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


class RecipeList(View):
    """Полный список рецептов на сайте"""
    def get(self, request):
        context = {
            'recipes': Recipe.objects.order_by('-created')
        }
        return render(request, template_name='main_recipe/recipe_list.html', context=context)
