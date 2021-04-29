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