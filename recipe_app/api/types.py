import graphene
from graphene_django.types import DjangoObjectType
from ..models import (Category,
                      Ingredient,
                      Recipe,
                      RecipeReview,
                      RecipeImage,
                      Topic,
                      TopicReview,
                      TopicImage,
                      Copyright)


class CopyrightType(DjangoObjectType):

    class Meta:
        model = Copyright
        fields = '__all__'


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        fields = '__all__'


class IngredientType(DjangoObjectType):

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeType(DjangoObjectType):

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeReviewType(DjangoObjectType):

    class Meta:
        model = RecipeReview
        fields = '__all__'


class RecipeImageType(DjangoObjectType):

    class Meta:
        model = RecipeImage
        fields = '__all__'


class TopicType(DjangoObjectType):

    class Meta:
        model = Topic
        fields = '__all__'


class TopicReviewType(DjangoObjectType):

    class Meta:
        model = TopicReview
        fields = '__all__'


class TopicImageType(DjangoObjectType):

    class Meta:
        model = TopicImage
        fields = '__all__'
