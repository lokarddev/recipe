from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import *
from .forms import TopicCommentForm, RecipeCommentForm, UserForm, AddRecipeForm
from django.urls import reverse


class HomeView(View):
    """Home page of a website, includes topics/recipes"""
    def get(self, request):
        context = {
            'topics': Topic.objects.filter(draft=False)[:3],
            'recipes': Recipe.objects.filter(draft=False)[:3]
        }
        return render(request, template_name='main_recipe/home.html', context=context)


class CategoryView(View):
    """Category list"""
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, template_name='main_recipe/category.html', context=context)


class GetData:
    """Handling recipe"""
    @staticmethod
    def get_ingredient():
        return Ingredient.objects.all()


class ConstructorView(GetData, ListView):
    """Filter implementation for searching specific recipe"""
    model = Recipe
    template_name = 'main_recipe/constructor.html'
    queryset = Recipe.objects.filter(draft=False)


class FilterView(View):
    """
    View provides rendering result from constructor post request
    """
    def get_queryset(self):
        queryset = Recipe.objects.filter(
            ingredient__in=self.request.GET.getlist('ingredient')
        ).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        context = {
            'query': self.get_queryset()
        }
        print(context)
        return render(request, 'main_recipe/filter_result.html', context=context)


class TopicDetail(View):
    """Detailed description of selected topic"""
    def get(self, request, pk):
        topic = get_object_or_404(Topic, id=pk)
        context = {
            'topic': topic,
            'comments': topic.review.all()
        }
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class RecipeDetail(View):
    """Detailed description of selected recipe"""
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        context = {
            'recipe': recipe,
            'comments': recipe.review.all()
        }
        return render(request, template_name='main_recipe/recipe_detail.html', context=context)


class CategoryList(View):
    """List of all recipes for specific category"""
    def get(self, request, pk):
        context = {
            'recipes': Recipe.objects.filter(category__id=pk)
        }
        return render(request, template_name='main_recipe/category_list.html', context=context)


class TopicList(View):
    """Topic list with only published objects"""
    def get(self, request):
        context = {
            'topics': Topic.objects.order_by('-created').filter(draft=False)
        }
        return render(request, template_name='main_recipe/topic_list.html', context=context)


class RecipeList(GetData, ListView):
    """Recipe list with only published objects"""
    model = Recipe
    queryset = Recipe.objects.order_by('created').filter(draft=False)
    template_name = 'main_recipe/recipe_list.html'


class AddTopicReview(View):
    """Topic review controller"""
    def post(self, request, pk):
        comment = None
        topic = get_object_or_404(Topic, id=pk)
        context = {
            'topic': topic,
            'comments': topic.review.all(),
            'comment': comment
        }
        form = TopicCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.save()
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class AddRecipeReview(View):
    """Recipe review controller"""
    def post(self, request, pk):
        review = None
        recipe = get_object_or_404(Recipe, id=pk)
        context = {
            'topic': recipe,
            'comments': recipe.review.all(),
            'comment': review
        }
        form = RecipeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class SearchView(ListView):
    """Searching from all recipes"""
    model = Recipe
    template_name = 'main_recipe/search_list.html'

    def get_queryset(self):
        """Обработка запроса с фронтенда (в виде введенного пользователем текста) и фильтрация"""
        query = self.request.GET.get('search')
        recipe_list = Recipe.objects.filter(
            recipe_title__icontains=query
        )
        return recipe_list


class UserProfile(LoginRequiredMixin, View):
    """Base user profile page"""
    login_url = '/login/'
    permission_denied_message = 'Вам не доступна данная страница'
    redirect_field_name = 'user_profile'

    def get(self, request):
        return render(request, template_name='main_recipe/user_profile.html')


class AddRecipe(View):
    """Adding new recipe"""
    def get(self, request):
        context = {
            'form': AddRecipeForm
        }
        return render(request, template_name='main_recipe/add_recipe.html', context=context)

    def post(self, request):
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_profile'))
