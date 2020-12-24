from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/home.html', context=context)


class CategoryView(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/category.html', context=context)


class ConstructorView(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='main_recipe/constructor.html', context=context)


class AboutView(View):
    def get(self, request):
        title = AboutInfo.objects.get(pk=1)
        context = {
            'about_title': title.about_title,
            'about_text': title.about_text
        }
        return render(request, template_name='main_recipe/about.html', context=context)
