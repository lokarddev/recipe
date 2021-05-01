from recipe_app.api.inputs import IngredientInput
from recipe_app.api.types import IngredientType
from recipe_app.models import Ingredient
from recipe_app.api.data import ingredient_create, ingredient_update
import graphene


class CreateIngredient(graphene.Mutation):

    class Arguments:
        data = IngredientInput()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, data=None):
        ingredient = ingredient_create(data)
        return CreateIngredient(ingredient=ingredient)


class UpdateIngredient(graphene.Mutation):

    class Arguments:
        data = IngredientInput()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, data=None):
        ingredient = ingredient_update(data)
        return ingredient


class DeleteIngredient(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredient_instance = Ingredient.objects.get(pk=id)
        ingredient_instance.delete()
        return None
