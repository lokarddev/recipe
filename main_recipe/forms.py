from .models import *
from django import forms


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
