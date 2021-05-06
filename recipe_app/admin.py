from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.admin import UserAdmin


class GetImage:
    """Image for field in admin panel"""
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50">')

    get_image.short_description = 'Image'


class Publicate:
    """Publicate or depublicate object"""
    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = '1 rows updated'
        else:
            message_bit = f'{row_update} rows updated'
        self.message_user(request, f'{message_bit}')

    def unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = '1 row added'
        else:
            message_bit = f'{row_update} rows updated'
        self.message_user(request, f'{message_bit}')

    def message_user(self, request, param):
        pass

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change',)
    unpublished.short_description = 'Unpublish'
    unpublished.allowed_permissions = ('change',)


class CopyrightAdmin(SummernoteModelAdmin):
    """Copyrights"""
    list_display = ('copyright_title', 'copyright_link', 'modified')
    list_display_links = ('copyright_title',)
    summernote_fields = '__all__'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin, GetImage):
    """Ingredients admin panel"""
    list_display = ('title', 'get_image')
    list_display_links = ('title',)


class RecipeAdmin(SummernoteModelAdmin, Publicate):
    """Recipe admin panel"""
    list_display = ('recipe_title', 'category', 'draft', 'modified')
    list_display_links = ('recipe_title', 'category')
    list_filter = ('category', 'ingredient')
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish', 'unpublished']
    summernote_fields = '__all__'


class TopicAdmin(SummernoteModelAdmin, Publicate):
    """Topic admin panel"""
    list_display = ('topic_title', 'draft', 'modified')
    list_display_links = ('topic_title',)
    list_filter = ('created',)
    list_editable = ('draft',)
    save_as = True
    save_on_top = True
    actions = ['publish', 'unpublished']
    summernote_fields = '__all__'


class CategoryAdmin(SummernoteModelAdmin, GetImage):
    """Category admin panel"""
    list_display = ('title', 'get_image')
    list_display_links = ('title',)
    extra = 1
    summernote_fields = '__all__'


@admin.register(TopicReview)
class TopicReviewAdmin(admin.ModelAdmin):
    """Topic review admin panel"""
    list_display = ('name', 'email', 'topic', 'created')
    list_display_links = ('topic',)
    list_filter = ('topic', 'created')


@admin.register(RecipeReview)
class RecipeReviewAdmin(admin.ModelAdmin):
    """Recipe review admin panel"""
    list_display = ('name', 'email', 'recipe', 'created')
    list_display_links = ('recipe',)
    list_filter = ('recipe', 'created')


admin.site.site_title = 'Recipe project'
admin.site.site_header = 'Recipe project'

# registering admin classes with summernote inheritance
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Copyright, CopyrightAdmin)
admin.site.register(CustomUser, UserAdmin)
