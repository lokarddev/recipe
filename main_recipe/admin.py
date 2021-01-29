from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Copyright, SomeModelAdmin)
admin.site.register(Ingredient, SomeModelAdmin)
admin.site.register(Recipe, SomeModelAdmin)
admin.site.register(Topic, SomeModelAdmin)
admin.site.register(Category, SomeModelAdmin)
admin.site.register(RecipeImage)
admin.site.register(TopicImage)
admin.site.register(TopicReview)
admin.site.register(RecipeReview)

