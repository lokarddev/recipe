from ..inputs import RecipeImageInput
from ..types import RecipeImageType
from recipe_app.models import RecipeImage
import graphene


class CreateRecipeImage(graphene.Mutation):

    class Arguments:
        recipe_image_data = RecipeImageInput()

    recipe_image = graphene.Field(RecipeImageType)

    @classmethod
    def mutate(cls, root, info, recipe_image_data=None):
        recipe_image_instance = RecipeImage(
            title=recipe_image_data.title,
            image=recipe_image_data.image
        )
        recipe_image_instance.save()
        return CreateRecipeImage(recipe_image=recipe_image_instance)


class DeleteRecipeImage(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    recipe_image = graphene.Field(RecipeImageType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe_image_instance = RecipeImage.objects.get(pk=id)
        recipe_image_instance.delete()
        return None
