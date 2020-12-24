from .models import *


def add_variable(request):
    return {
        'copyrights': CopyrightInfo.objects.get(pk=1)
    }
