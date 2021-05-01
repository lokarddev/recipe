from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class GetImage:
    """Изображение для записи в списке админки"""
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50">')

    get_image.short_description = 'Изображение'


class Publicate:
    """Публикация или снятие публикации записи"""
    def publish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлено'
        self.message_user(request, f'{message_bit}')

    def unpublished(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлено'
        self.message_user(request, f'{message_bit}')

    def message_user(self, request, param):
        pass

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)
    unpublished.short_description = 'Снять с публикации'
    unpublished.allowed_permissions = ('change',)


class RecipeReviewInline(admin.TabularInline):
    """Отображение отзыва рецепта в других моделях (related objects)"""
    pass


class TopicReviewInline(admin.TabularInline):
    """Отображение отзыва статьи в других моделях (related objects)"""
    pass


class CopyrightAdmin(SummernoteModelAdmin):
    """Авторские права"""
    list_display = ('copyright_title', 'copyright_link', 'modified')
    list_display_links = ('copyright_title',)
    summernote_fields = '__all__'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin, GetImage):
    """Ингредиенты"""
    list_display = ('title', 'get_image')
    list_display_links = ('title',)


class RecipeAdmin(SummernoteModelAdmin, Publicate):
    """Рецепты"""
    list_display = ('recipe_title', 'category', 'draft', 'modified')
    list_display_links = ('recipe_title', 'category')
    list_filter = ('category', 'ingredient')
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish', 'unpublished']
    summernote_fields = '__all__'


class TopicAdmin(SummernoteModelAdmin, Publicate):
    """Статьи"""
    list_display = ('topic_title', 'draft', 'modified')
    list_display_links = ('topic_title',)
    list_filter = ('created',)
    list_editable = ('draft',)
    save_as = True
    save_on_top = True
    actions = ['publish', 'unpublished']
    summernote_fields = '__all__'


class CategoryAdmin(SummernoteModelAdmin, GetImage):
    """Категории рецептов"""
    list_display = ('title', 'get_image')
    list_display_links = ('title',)
    extra = 1
    summernote_fields = '__all__'


@admin.register(TopicReview)
class TopicReviewAdmin(admin.ModelAdmin):
    """Отзыв о статье"""
    list_display = ('name', 'email', 'topic', 'created')
    list_display_links = ('topic',)
    list_filter = ('topic', 'created')


@admin.register(RecipeReview)
class RecipeReviewAdmin(admin.ModelAdmin):
    """Отзыв о рецепте"""
    list_display = ('name', 'email', 'recipe', 'created')
    list_display_links = ('recipe',)
    list_filter = ('recipe', 'created')


admin.site.site_title = 'Recipe project'
admin.site.site_header = 'Recipe project'

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Copyright, CopyrightAdmin)
