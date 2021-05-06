import graphene
from graphene_file_upload.scalars import Upload


class CategoryInput(graphene.InputObjectType):
    """Input fields for category model"""
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    image = Upload()


class IngredientInput(graphene.InputObjectType):
    """Input fields for ingredient model"""
    id = graphene.ID()
    description = graphene.String()
    image = Upload()


class RecipeInput(graphene.InputObjectType):
    """Input fields for recipe model"""
    id = graphene.ID()
    recipe_title = graphene.String()
    recipe_text = graphene.String()
    category = graphene.Field(CategoryInput)
    url = graphene.String()
    draft = graphene.Boolean(default=True)
    ingredient = graphene.String()
    image = Upload(required=False)


class RecipeReviewInput(graphene.InputObjectType):
    """Input fields for recipe review model"""
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    recipe = graphene.Field(RecipeInput)


class TopicInput(graphene.InputObjectType):
    """Input fields for topic model"""
    id = graphene.ID()
    topic_title = graphene.String()
    topic_text = graphene.String()
    recipe = graphene.Field(RecipeInput)
    url = graphene.String()
    draft = graphene.Boolean(default=True)
    image = Upload()


class TopicReviewInput(graphene.InputObjectType):
    """Input fields for topic review model"""
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    topic = graphene.Field(TopicInput)
