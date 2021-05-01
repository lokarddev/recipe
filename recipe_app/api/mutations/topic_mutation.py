from recipe_app.api.inputs import TopicInput
from recipe_app.api.types import TopicType
from recipe_app.models import Topic
from recipe_app.api.data import topic_create, topic_update
import graphene


class CreateTopic(graphene.Mutation):

    class Arguments:
        data = TopicInput()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, data=None):
        topic = topic_create(data)
        return CreateTopic(topic=topic)


class UpdateTopic(graphene.Mutation):

    class Arguments:
        data = TopicInput()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, data=None):
        topic = topic_update(data)
        return UpdateTopic(topic=topic)


class DeleteTopic(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, id):
        topic_instance = Topic.objects.get(pk=id)
        topic_instance.delete()
        return None
