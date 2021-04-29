from ..inputs import CategoryInput
from ..types import CategoryType
from recipe_app.models import Category
import graphene


class CreateCategory(graphene.Mutation):

    class Arguments:
        category_data = CategoryInput()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, category_data=None):
        category_instance = Category(
            title=category_data.title,
            description=category_data.description,
            image=category_data.image
        )
        category_instance.save()
        return CreateCategory(category=category_instance)


class UpdateCategory(graphene.Mutation):

    class Arguments:
        category_data = CategoryInput()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, category_data=None):
        category_instance = Category.objects.get(pk=category_data.id)

        if category_instance:
            category_instance.title = category_data.title
            category_instance.description = category_data.description
            category_instance.image = category_data.image
            category_instance.save()

            return UpdateCategory(category=category_instance)
        return UpdateCategory(category=None)


class DeleteCategory(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category_instance = Category.objects.get(pk=id)
        category_instance.delete()
        return None
