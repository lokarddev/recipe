from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, template_name='main_recipe/home.html')


class Category(View):
    def get(self, request):
        return render(request, template_name='main_recipe/category.html')


class Constructor(View):
    def get(self, request):
        return render(request, template_name='main_recipe/constructor.html')


class About(View):
    def get(self, request):
        return render(request, template_name='main_recipe/about.html')
