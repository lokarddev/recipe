from django.shortcuts import render
from django.views import View
from models import *


class Home(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/home.html', context=context)


class Category(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/category.html', context=context)


class Constructor(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/constructor.html', context=context)


class About(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/about.html', context=context)
