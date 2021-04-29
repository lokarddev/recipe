import graphene


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()


class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    description = graphene.String()
    image = graphene.String()


class RecipeInput(graphene.InputObjectType):
    id = graphene.ID()
    recipe_title = graphene.String()
    recipe_text = graphene.String()
    category = graphene.String()
    url = graphene.String()
    draft = graphene.Boolean()
    ingredient = graphene.String()
    image = graphene.String()


class RecipeReviewInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    recipe = graphene.String()


class RecipeImageInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    image = graphene.String()


class TopicInput(graphene.InputObjectType):
    id = graphene.ID()
    topic_title = graphene.String()
    topic_text = graphene.String()
    recipe = graphene.String()
    url = graphene.String()
    draft = graphene.Boolean()
    image = graphene.String()


class TopicReviewInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()
    topic = graphene.String()


class TopicImageInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    image = graphene.String()
