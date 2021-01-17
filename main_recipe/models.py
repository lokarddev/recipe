from django.db import models


class Copyright(models.Model):
    """Information about copyrights in FOOTER of the site"""
    copyright_title = models.CharField(max_length=150)
    copyright_text = models.TextField()
    copyright_link = models.CharField(max_length=100)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.copyright_title

    def __str__(self):
        return self.copyright_title


class Ingredient(models.Model):
    """The name of ingredient used in a recipe"""
    product_title = models.CharField(max_length=50)

    def __repr__(self):
        return self.product_title

    def __str__(self):
        return self.product_title


class Category(models.Model):
    """All available categories"""
    title = models.CharField('Category', max_length=100)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Recipe itself"""
    recipe_title = models.CharField(max_length=100)
    recipe_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return self.recipe_title

    def __str__(self):
        return self.recipe_title


class Topic(models.Model):
    """Random topic with content. Able to have "recipe model" info inside"""
    topic_title = models.CharField(max_length=150)
    topic_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.topic_title

    def __str__(self):
        return self.topic_title
