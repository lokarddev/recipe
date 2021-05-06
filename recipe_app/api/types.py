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
from recipe_app.api.redis_logic import click


class CopyrightType(DjangoObjectType):
    """Converting copyright model object to graphene style object type"""

    class Meta:
        model = Copyright
        fields = '__all__'


class CategoryType(DjangoObjectType):
    """Converting category model object to graphene style object type"""

    class Meta:
        model = Category
        filter_fields = ['id', 'title']
        interfaces = (relay.Node, )


class IngredientType(DjangoObjectType):
    """Converting ingredient model object to graphene style object type"""

    class Meta:
        model = Ingredient
        filter_fields = ['id', 'title']
        interfaces = (relay.Node, )


class RecipeType(DjangoObjectType):
    """Converting recipe model object to graphene style object type"""

    class Meta:
        model = Recipe
        filter_fields = ['id', 'recipe_title', 'category', 'url', 'draft', 'ingredient', 'created']
        interfaces = (relay.Node, )


class RecipeReviewType(DjangoObjectType):
    """Converting recipe review model object to graphene style object type"""

    class Meta:
        model = RecipeReview
        filter_fields = ['id', 'name', 'email', 'recipe', 'created']
        interfaces = (relay.Node, )


class TopicType(DjangoObjectType):
    """Converting topic model object to graphene style object type"""

    class Meta:
        model = Topic
        filter_fields = ['id', 'topic_title', 'created', 'recipe', 'url', 'draft']
        interfaces = (relay.Node, )


class TopicReviewType(DjangoObjectType):
    """Converting topic review model object to graphene style object type"""

    class Meta:
        model = TopicReview
        filter_fields = ['id', 'name', 'email', 'topic', 'created']
        interfaces = (relay.Node, )


class ClickStatType(graphene.Scalar):
    """Creating object type to get graphql access to click detail mutation"""

    @classmethod
    def serialize(cls, *args, **kwargs):
        return click.get_click()
