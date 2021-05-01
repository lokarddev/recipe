from recipe_app.api.inputs import RecipeReviewInput
from recipe_app.api.types import RecipeReviewType
from recipe_app.models import RecipeReview, Recipe
from recipe_app.api.data import recipe_review_create
import graphene


class CreateRecipeReview(graphene.Mutation):

    class Arguments:
        data = RecipeReviewInput()

    recipe_review = graphene.Field(RecipeReviewType)

    @classmethod
    def mutate(cls, root, info, data=None):
        recipe_review = recipe_review_create(data)
        return CreateRecipeReview(recipe_review=recipe_review)


class DeleteRecipeReview(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    recipe_review = graphene.Field(RecipeReviewType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe_review_instance = RecipeReview.objects.get(pk=id)
        recipe_review_instance.delete()
        return None
