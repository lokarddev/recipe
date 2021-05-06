import graphene
from recipe_app.api.types import ClickStatType
from recipe_app.api.redis_logic import click


class ClickDetail(graphene.Mutation):

    click_amount = graphene.Field(ClickStatType)

    @classmethod
    def mutate(cls, root, info):
        click.incr_click()
        amount = {'click': click.get_click()}
        return ClickDetail(click_amount=amount)
