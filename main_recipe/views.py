from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    """The main page of the site. Contains the latest 4 recipes as table of cards"""
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/home.html', context=context)


class CategoryView(View):
    """Category page with a table of cards ordered by their category. Every card is a link contains a list of recipes"""
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/category.html', context=context)


class ConstructorView(View):
    """The main feature of the site. Basically works as simple filter page at e-commerce. Contains table of categories
    and list of products to choose from"""
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/constructor.html', context=context)


class AboutView(View):
    """Single page with information about the project"""
    def get(self, request):
        title = AboutInfo.objects.get(pk=1)
        context = {
            'about_title': title.about_title,
            'about_text': title.about_text
        }
        return render(request, template_name='main_recipe/about.html', context=context)
