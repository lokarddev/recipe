from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class TopicCommentForm(forms.ModelForm):
    """Форма комментария статьи"""
    class Meta:
        model = TopicReview
        fields = ('name', 'email', 'body')


class RecipeCommentForm(forms.ModelForm):
    """Форма для комментария рецепта"""
    class Meta:
        model = RecipeReview
        fields = ('name', 'email', 'body')


class UserForm(UserCreationForm):
    """Форма создания пользователя"""
    class Meta(UserCreationForm.Meta):
        """Дополнительное поле 'почта' при создании"""
        fields = UserCreationForm.Meta.fields + ('email',)


class AddRecipeForm(forms.ModelForm):
    """Форма добавления собственного рецепта пользователем"""
    class Meta:
        model = Recipe
        fields = ('recipe_title', 'recipe_text', 'category', 'ingredient')
