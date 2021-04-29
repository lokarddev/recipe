from ..inputs import IngredientInput
from ..types import IngredientType
from recipe_app.models import Ingredient
import graphene


class CreateIngredient(graphene.Mutation):

    class Arguments:
        ingredient_data = IngredientInput()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, ingredient_data=None):
        ingredient_instance = Ingredient(
            description=ingredient_data.description,
            image=ingredient_data.image
        )
        ingredient_instance.save()
        return CreateIngredient(ingredient=ingredient_instance)


class UpdateIngredient(graphene.Mutation):

    class Arguments:
        ingredient_data = IngredientInput()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, ingredient_data=None):
        ingredient_instance = Ingredient.objects.get(pk=ingredient_data.id)

        if ingredient_instance:
            ingredient_instance.description = ingredient_data.description
            ingredient_instance.image = ingredient_data.image
            ingredient_instance.save()

            return UpdateIngredient(ingredient=ingredient_instance)
        return UpdateIngredient(ingredient=None)


class DeleteIngredient(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredient_instance = Ingredient.objects.get(pk=id)
        ingredient_instance.delete()
        return None
