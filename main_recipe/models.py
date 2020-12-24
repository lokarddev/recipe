from django.db import models


class Copyright(models.Model):
    """Information about copyrights in FOOTER of the site"""
    copyright_title = models.CharField(max_length=150)
    copyright_text = models.TextField()
    copyright_link = models.CharField(max_length=100)


class About(models.Model):
    """Topic with content at page ABOUT"""
    about_title = models.CharField(max_length=100)
    about_text = models.TextField()


class Product(models.Model):
    """The name of ingredient used in a recipe"""
    product_title = models.CharField(max_length=50)


class Recipe(models.Model):
    """Recipe itself"""
    recipe_title = models.CharField(max_length=100)
    recipe_text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now_add=True)


class Topic(models.Model):
    """Random topic with content. Able to have "recipe model" info inside"""
    topic_title = models.CharField(max_length=150)
    topic_text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now_add=True)
