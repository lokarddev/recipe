from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import *
from .forms import TopicCommentForm, RecipeCommentForm, UserForm, AddRecipeForm
from django.urls import reverse


class HomeView(View):
    """Главная страница сайта. Содержит две таблицы с данными рецептов/статей в виде карточек"""
    def get(self, request):
        context = {
            'topics': Topic.objects.all()[:3],
            'recipes': Recipe.objects.all()[:3]
        }
        return render(request, template_name='main_recipe/home.html', context=context)


class CategoryView(View):
    """Страница категорий рецептов"""
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
    """Основной страница фильтра рецептов по категориям и содержащимся продуктам. Отображает форму для фильтрации"""
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
    """Детальное описание выбранной статьи"""
    def get(self, request, pk):
        topic = get_object_or_404(Topic, id=pk)
        context = {
            'topic': Topic.objects.get(id=pk),
            'comments': topic.review.all()
        }
        return render(request, template_name='main_recipe/topic_detail.html', context=context)


class RecipeDetail(View):
    """Детальное описание выбранного рецепта"""
    def get(self, request, pk):
        context = {
            'recipe': Recipe.objects.get(id=pk),
        }
        return render(request, template_name='main_recipe/recipe_detail.html', context=context)


class CategoryList(View):
    """Список рецептов в выбранной категории"""
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
    queryset = Recipe.objects.order_by('created')


class AddTopicReview(View):
    """Контроллер отзыва к статье"""
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


class SearchView(ListView):
    """Поиск рецептов из общего списка"""
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
    """Страница профиля пользователя"""
    login_url = '/login/'
    permission_denied_message = 'Вам не доступна данная страница'
    redirect_field_name = 'user_profile'

    def get(self, request):
        return render(request, template_name='main_recipe/user_profile.html')


class Register(View):
    """Страница регистрации"""
    def get(self, request):
        context ={
            'form': UserForm
        }
        return render(request, template_name='registration/user.html', context=context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))


class AddRecipe(View):
    """Добавление нового рецепта"""
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
