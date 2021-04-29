from ..inputs import RecipeInput
from ..types import RecipeType
from recipe_app.models import Recipe
import graphene


class CreateRecipe(graphene.Mutation):

    class Arguments:
        recipe_data = RecipeInput()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, recipe_data=None):
        recipe_instance = Recipe(
            recipe_title=recipe_data.recipe_title,
            recipe_text=recipe_data.recipe_text,
            category=recipe_data.category,
            url=recipe_data.url,
            draft=recipe_data.draft,
            image=recipe_data.image
        )
        recipe_instance.save()
        return CreateRecipe(recipe=recipe_instance)


class UpdateRecipe(graphene.Mutation):

    class Arguments:
        recipe_data = RecipeInput()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, recipe_data=None):
        recipe_instance = Recipe.objects.get(pk=recipe_data.id)

        if recipe_instance:
            recipe_instance.recipe_title = recipe_data.recipe_title,
            recipe_instance.recipe_text = recipe_data.recipe_text,
            recipe_instance.category = recipe_data.category,
            recipe_instance.url = recipe_data.url,
            recipe_instance.draft = recipe_data.draft,
            recipe_instance.image = recipe_data.image
            recipe_instance.save()

            return UpdateRecipe(recipe=recipe_instance)
        return UpdateRecipe(recipe=None)


class DeleteRecipe(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe_instance = Recipe.objects.get(pk=id)
        recipe_instance.delete()
        return None
