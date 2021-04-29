from ..inputs import TopicInput
from ..types import TopicType
from recipe_app.models import Topic
import graphene


class CreateTopic(graphene.Mutation):

    class Arguments:
        recipe_data = TopicInput()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, topic_data=None):
        topic_instance = Topic(
            topic_title=topic_data.topic_title,
            topic_text=topic_data.topic_text,
            recipe=topic_data.recipe,
            url=topic_data.url,
            draft=topic_data.draft
        )
        topic_instance.save()
        return CreateTopic(topic=topic_instance)


class UpdateTopic(graphene.Mutation):

    class Arguments:
        topic_data = TopicInput()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, topic_data=None):
        topic_instance = Topic.objects.get(pk=topic_data.id)

        if topic_instance:
            topic_instance.topic_title = topic_data.topic_title,
            topic_instance.topic_text = topic_data.topic_text,
            topic_instance.recipe = topic_data.recipe,
            topic_instance.url = topic_data.url,
            topic_instance.draft = topic_data.draft
            topic_instance.save()

            return UpdateTopic(topic=topic_instance)
        return UpdateTopic(topic=None)


class DeleteTopic(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    topic = graphene.Field(TopicType)

    @classmethod
    def mutate(cls, root, info, id):
        topic_instance = Topic.objects.get(pk=id)
        topic_instance.delete()
        return None
