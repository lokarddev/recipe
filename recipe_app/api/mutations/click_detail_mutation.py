import graphene
from recipe_app.api.types import ClickStatType
from recipe_app.api.redis_logic import Click


class ClickDetail(graphene.Mutation):

    click_amount = graphene.Field(ClickStatType)

    @classmethod
    def mutate(cls, root, info):
        Click.incr_click()
        amount = {'click': Click.get_click()}
        return ClickDetail(click_amount=amount)
