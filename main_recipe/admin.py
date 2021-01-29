from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# админ-модель редактора текста и переопределение всех textfield в других моделях
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

