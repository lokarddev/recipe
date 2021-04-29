import graphene
from .types import *
from mutations import *
from ..models import (Category,
                      Ingredient,
                      Recipe,
                      RecipeReview,
                      RecipeImage,
                      Topic,
                      TopicReview,
                      TopicImage,
                      Copyright)


class Query(graphene.ObjectType):
    category = graphene.Field(CategoryType, category_id=graphene.Int())
    categories = graphene.List(CategoryType)

    def resolve_category(self, info, **kwargs):
        category_id = kwargs.get('category_id')
        if category_id is not None:
            return Category.objects.get(title=category_id)
        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)