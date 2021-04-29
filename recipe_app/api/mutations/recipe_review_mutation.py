from ..inputs import RecipeReviewInput
from ..types import RecipeReviewType
from recipe_app.models import RecipeReview, Recipe
import graphene


class CreateRecipeReview(graphene.Mutation):

    class Arguments:
        recipe_review_data = RecipeReviewInput()

    recipe_review = graphene.Field(RecipeReviewType)

    @classmethod
    def mutate(cls, root, info, recipe_review_data=None):
        recipe = Recipe.objects.get(recipe_title=recipe_review_data.recipe)
        recipe_review_instance = RecipeReview(
            name=recipe_review_data.name,
            email=recipe_review_data.email,
            body=recipe_review_data.body,
            recipe=recipe
        )
        recipe_review_instance.save()
        return CreateRecipeReview(recipe_review=recipe_review_instance)


class DeleteRecipeReview(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    recipe_review = graphene.Field(RecipeReviewType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe_review_instance = RecipeReview.objects.get(pk=id)
        recipe_review_instance.delete()
        return None
