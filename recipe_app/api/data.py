from recipe_app.models import Recipe, Category, Topic, TopicReview, RecipeReview, Ingredient


# this file provides more structured model manipulation in mutations


def recipe_create(data):
    """Create new recipe with graphql"""
    recipe = Recipe(
        recipe_title=data.recipe_title,
        recipe_text=data.recipe_text,
        url=data.url,
        image=data.image,
        category=Category.objects.get(pk=data.category['id'])
    )
    recipe.save()
    return recipe


def recipe_update(data):
    """Update recipe with graphql"""
    recipe = Recipe.objects.get(pk=data.id)
    if recipe:
        for item in data:
            recipe.item = item
        recipe.save()
        return recipe
    return None


def recipe_review_create(data):
    """Create new recipe review with graphql"""
    recipe = Recipe.objects.get(recipe_title=data.recipe)
    recipe_review_instance = RecipeReview(
            name=data.name,
            body=data.body,
            recipe=Recipe.objects.get(pk=data.recipe['id'])
        )
    recipe_review_instance.save()
    return recipe_review_instance


def topic_create(data):
    """Create new topic with graphql"""
    topic_recipe = Recipe.objects.filter(pk=data.recipe['id'])
    topic = Topic(
        topic_title=data.topic_title,
        topic_text=data.topic_text,
        url=data.url,
    )
    topic.save()
    topic.recipe.set(topic_recipe)
    return topic


def topic_update(data):
    """Update topic with graphql"""
    topic = Topic.objects.get(pk=data.id)
    if topic:
        for item in data:
            topic.item = item
        topic.save()
        return topic
    return None


def topic_review_create(data):
    """Create new topic review with graphql"""
    topic_review = TopicReview(
        name=data.name,
        body=data.body,
        topic=Topic.objects.get(pk=data.topic['id'])
    )
    topic_review.save()
    return topic_review


def ingredient_create(data):
    """Create new recipe with graphql"""
    ingredient = Ingredient(
        description=data.description,
        image=data.image
    )
    ingredient.save()
    return ingredient


def ingredient_update(data):
    """Create new recipe with graphql"""
    ingredient = Ingredient.objects.get(pk=data.id)
    if ingredient:
        for item in data:
            ingredient.item = item
        ingredient.save()
        return ingredient
    return None


def category_create(data):
    """Create new recipe with graphql"""
    category = Category(
        title=data.title,
        description=data.description,
        image=data.image
    )
    category.save()


def category_update(data):
    """Create new recipe with graphql"""
    category = Category.objects.get(pk=data.id)
    if category:
        for item in data:
            category.item = item
        category.save()
        return category
    return None
