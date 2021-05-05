from recipe_app.api.redis_logic import Click
from recipe_app.models import ClickStat
from celery import Celery, shared_task


@shared_task()
def click_to_model():
    stat_point = ClickStat(
        amount=Click.get_click()
    )
    stat_point.save()
    Click.reset_click()
