import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import *
from graphene import relay
from .mutations import *


class Query(graphene.ObjectType):

    category = relay.Node.Field(CategoryType)
    categories = DjangoFilterConnectionField(CategoryType)

    ingredient = relay.Node.Field(IngredientType)
    ingredients = DjangoFilterConnectionField(IngredientType)

    recipe = relay.Node.Field(RecipeType)
    recipes = DjangoFilterConnectionField(RecipeType)

    recipe_review = relay.Node.Field(RecipeReviewType)
    recipe_reviews = DjangoFilterConnectionField(RecipeReviewType)

    recipe_image = relay.Node.Field(RecipeImageType)
    recipe_images = DjangoFilterConnectionField(RecipeImageType)

    topic = relay.Node.Field(TopicType)
    topics = DjangoFilterConnectionField(TopicType)

    topic_review = relay.Node.Field(TopicReviewType)
    topic_reviews = DjangoFilterConnectionField(TopicReviewType)

    topic_image = relay.Node.Field(TopicImageType)
    topic_images = DjangoFilterConnectionField(TopicImageType)

# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)