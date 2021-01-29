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
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_title', 'recipe_text', 'category', 'ingredient')
