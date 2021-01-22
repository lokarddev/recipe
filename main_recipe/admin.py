from django.contrib import admin
from .models import *


admin.site.register(Copyright)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(RecipeImage)
admin.site.register(TopicImage)
