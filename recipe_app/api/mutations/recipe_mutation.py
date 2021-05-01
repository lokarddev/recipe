from recipe_app.api.inputs import RecipeInput
from recipe_app.api.types import RecipeType
from recipe_app.models import Recipe, Category
import graphene
from recipe_app.api.data import recipe_create, recipe_update


class CreateRecipe(graphene.Mutation):
    recipe = graphene.Field(RecipeType)

    class Arguments:
        data = RecipeInput()

    @classmethod
    def mutate(cls, root, info, data=None):
        recipe = recipe_create(data)
        return CreateRecipe(recipe=recipe)


class UpdateRecipe(graphene.Mutation):

    recipe = graphene.Field(RecipeType)

    class Arguments:
        data = RecipeInput()

    @classmethod
    def mutate(cls, root, info, data=None):

        recipe = recipe_update(data)

        return UpdateRecipe(recipe=recipe)


class DeleteRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe_instance = Recipe.objects.get(pk=id)
        recipe_instance.delete()
        return None
