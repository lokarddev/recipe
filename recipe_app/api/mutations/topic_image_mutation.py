from ..inputs import TopicImageInput
from ..types import TopicImageType
from recipe_app.models import TopicImage
import graphene


class CreateTopicImage(graphene.Mutation):

    class Arguments:
        topic_image_data = TopicImageInput()

    topic_image = graphene.Field(TopicImageType)

    @classmethod
    def mutate(cls, root, info, topic_image_data=None):
        topic_image_instance = TopicImage(
            title=topic_image_data.title,
            image=topic_image_data.image
        )
        topic_image_instance.save()
        return CreateTopicImage(topic_image=topic_image_instance)


class DeleteTopicImage(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    topic_image = graphene.Field(TopicImageType)

    @classmethod
    def mutate(cls, root, info, id):
        topic_image_instance = TopicImage.objects.get(pk=id)
        topic_image_instance.delete()
        return None
