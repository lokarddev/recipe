import graphene
import graphql_jwt
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from .types import (CategoryType,
                    IngredientType,
                    RecipeType,
                    RecipeReviewType,
                    TopicType,
                    TopicReviewType,)
from .mutations import (category_mutation,
                        ingredient_mutation,
                        recipe_mutation,
                        recipe_review_mutation,
                        topic_mutation,
                        topic_review_mutation)


class Query(graphene.ObjectType):

    category = relay.Node.Field(CategoryType)
    categories = DjangoFilterConnectionField(CategoryType)

    ingredient = relay.Node.Field(IngredientType)
    ingredients = DjangoFilterConnectionField(IngredientType)

    recipe = relay.Node.Field(RecipeType)
    recipes = DjangoFilterConnectionField(RecipeType)

    recipe_review = relay.Node.Field(RecipeReviewType)
    recipe_reviews = DjangoFilterConnectionField(RecipeReviewType)

    topic = relay.Node.Field(TopicType)
    topics = DjangoFilterConnectionField(TopicType)

    topic_review = relay.Node.Field(TopicReviewType)
    topic_reviews = DjangoFilterConnectionField(TopicReviewType)


class Mutation(graphene.ObjectType):

    create_category = category_mutation.CreateCategory.Field()
    update_category = category_mutation.UpdateCategory.Field()
    delete_category = category_mutation.DeleteCategory.Field()

    create_ingredient = ingredient_mutation.CreateIngredient.Field()
    update_ingredient = ingredient_mutation.UpdateIngredient.Field()
    delete_ingredient = ingredient_mutation.DeleteIngredient.Field()

    create_recipe = recipe_mutation.CreateRecipe.Field()
    update_recipe = recipe_mutation.UpdateRecipe.Field()
    delete_recipe = recipe_mutation.DeleteRecipe.Field()

    create_recipe_review = recipe_review_mutation.CreateRecipeReview.Field()
    delete_recipe_review = recipe_review_mutation.DeleteRecipeReview.Field()

    create_topic = topic_mutation.CreateTopic.Field()
    update_topic = topic_mutation.UpdateTopic.Field()
    delete_topic = topic_mutation.DeleteTopic.Field()

    create_topic_review = topic_review_mutation.CreateTopicReview.Field()
    delete_topic_review = topic_review_mutation.DeleteTopicReview.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
