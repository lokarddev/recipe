from .models import *
from django.core.exceptions import ObjectDoesNotExist
# we use this file for managing the template variables and creating new carries remotely here


def add_variable(request):
    try:
        return {
            'copyrights': Copyright.objects.latest('modified')
        }
    # for situations when we haven't any objects at the table.
    except ObjectDoesNotExist:
        return {}
