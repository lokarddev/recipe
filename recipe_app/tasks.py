from recipe_app.api.redis_logic import click
from recipe_app.models import ClickStat
from celery import shared_task


@shared_task()
def click_to_model():
    """Task provides dumping of redis 'click' data to a database model 'ClickStat' and reset it's amount"""
    stat_point = ClickStat(
        amount=click.get_click()
    )
    stat_point.save()
    click.reset_click()
