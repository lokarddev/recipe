from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class TopicCommentForm(forms.ModelForm):
    """Topic review comment form"""
    class Meta:
        model = TopicReview
        fields = ('name', 'body')


class RecipeCommentForm(forms.ModelForm):
    """Recipe review comment form"""
    class Meta:
        model = RecipeReview
        fields = ('name', 'body')


class UserForm(UserCreationForm):
    """Base user creation form"""
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class AddRecipeForm(forms.ModelForm):
    """Recipe add form"""
    class Meta:
        model = Recipe
        fields = ('recipe_title', 'recipe_text', 'category', 'ingredient', 'image')
