import graphene
from graphene_file_upload.scalars import Upload


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    image = Upload()


class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    description = graphene.String()
    image = Upload()


class RecipeInput(graphene.InputObjectType):
    id = graphene.ID()
    recipe_title = graphene.String()
    recipe_text = graphene.String()
    category = graphene.Field(CategoryInput)
    url = graphene.String()
    draft = graphene.Boolean(default=True)
    ingredient = graphene.String()
    image = Upload(required=False)


class RecipeReviewInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    recipe = graphene.Field(RecipeInput)


class TopicInput(graphene.InputObjectType):
    id = graphene.ID()
    topic_title = graphene.String()
    topic_text = graphene.String()
    recipe = graphene.Field(RecipeInput)
    url = graphene.String()
    draft = graphene.Boolean(default=True)
    image = Upload()


class TopicReviewInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    topic = graphene.Field(TopicInput)
