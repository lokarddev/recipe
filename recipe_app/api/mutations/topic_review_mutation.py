from recipe_app.api.inputs import TopicReviewInput
from recipe_app.api.types import TopicReviewType
from recipe_app.models import TopicReview
from recipe_app.api.data import topic_review_create
import graphene


class CreateTopicReview(graphene.Mutation):

    class Arguments:
        data = TopicReviewInput()

    topic_review = graphene.Field(TopicReviewType)

    @classmethod
    def mutate(cls, root, info, data=None):
        topic_review = topic_review_create(data)
        return CreateTopicReview(topic_review=topic_review)


class DeleteTopicReview(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    topic_review = graphene.Field(TopicReviewType)

    @classmethod
    def mutate(cls, root, info, id):
        topic_review_instance = TopicReview.objects.get(pk=id)
        topic_review_instance.delete()
        return None
