from ..inputs import TopicReviewInput
from ..types import TopicReviewType
from recipe_app.models import TopicReview
import graphene


class CreateTopicReview(graphene.Mutation):

    class Arguments:
        topic_review_data = TopicReviewInput()

    topic_review = graphene.Field(TopicReviewType)

    @classmethod
    def mutate(cls, root, info, topic_review_data=None):
        topic_review_instance = TopicReview(
            name=topic_review_data.name,
            email=topic_review_data.email,
            body=topic_review_data.body,
            topic=topic_review_data.topic
        )
        topic_review_instance.save()
        return CreateTopicReview(topic_review=topic_review_instance)


class DeleteTopicReview(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    topic_review = graphene.Field(TopicReviewType)

    @classmethod
    def mutate(cls, root, info, id):
        topic_review_instance = TopicReview.objects.get(pk=id)
        topic_review_instance.delete()
        return None
