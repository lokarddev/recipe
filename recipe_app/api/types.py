import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from ..models import (Category,
                      Ingredient,
                      Recipe,
                      RecipeReview,
                      Topic,
                      TopicReview,
                      Copyright)
from recipe_app.api.redis_logic import Click


class CopyrightType(DjangoObjectType):

    class Meta:
        model = Copyright
        fields = '__all__'


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        filter_fields = ['id', 'title']
        interfaces = (relay.Node, )


class IngredientType(DjangoObjectType):

    class Meta:
        model = Ingredient
        filter_fields = ['id', 'title']
        interfaces = (relay.Node, )


class RecipeType(DjangoObjectType):

    class Meta:
        model = Recipe
        filter_fields = ['id', 'recipe_title', 'category', 'url', 'draft', 'ingredient', 'created']
        interfaces = (relay.Node, )


class RecipeReviewType(DjangoObjectType):

    class Meta:
        model = RecipeReview
        filter_fields = ['id', 'name', 'email', 'recipe', 'created']
        interfaces = (relay.Node, )


class TopicType(DjangoObjectType):

    class Meta:
        model = Topic
        filter_fields = ['id', 'topic_title', 'created', 'recipe', 'url', 'draft']
        interfaces = (relay.Node, )


class TopicReviewType(DjangoObjectType):

    class Meta:
        model = TopicReview
        filter_fields = ['id', 'name', 'email', 'topic', 'created']
        interfaces = (relay.Node, )


class ClickStatType(graphene.Scalar):

    @classmethod
    def serialize(cls, *args, **kwargs):
        return Click.get_click()
