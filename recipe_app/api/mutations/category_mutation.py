from recipe_app.api.inputs import CategoryInput
from recipe_app.api.types import CategoryType
from recipe_app.models import Category
from recipe_app.api.data import category_create, category_update
import graphene


class CreateCategory(graphene.Mutation):

    class Arguments:
        data = CategoryInput()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, data=None):
        category = category_create(data)
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):

    class Arguments:
        data = CategoryInput()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, data=None):
        category = category_update(data)
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category_instance = Category.objects.get(pk=id)
        category_instance.delete()
        return None
