from .models import *
from django.core.exceptions import ObjectDoesNotExist


def add_variable(request):
    try:
        return {
            'copyrights': CopyrightInfo.objects.get(pk=1)
        }
    # for situations when we haven't any objects at the table.
    except ObjectDoesNotExist:
        return {}
