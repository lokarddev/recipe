from recipe_app.api.inputs import RecipeInput
from recipe_app.api.types import RecipeType
from recipe_app.models import Recipe, Category
import graphene
from recipe_app.api.data import recipe_create, recipe_update
from graphql_jwt.decorators import login_required


class CreateRecipe(graphene.Mutation):
    recipe = graphene.Field(RecipeType)

    class Arguments:
        data = RecipeInput()

    @classmethod
    @login_required
    def mutate(cls, root, info, data=None):
        recipe = recipe_create(data)
        return CreateRecipe(recipe=recipe)


class UpdateRecipe(graphene.Mutation):
    recipe = graphene.Field(RecipeType)

    class Arguments:
        data = RecipeInput()

    @classmethod
    @login_required
    def mutate(cls, root, info, data=None):
        recipe = recipe_update(data)

        return UpdateRecipe(recipe=recipe)


class DeleteRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id):
        recipe_instance = Recipe.objects.get(pk=id)
        recipe_instance.delete()
        return None
