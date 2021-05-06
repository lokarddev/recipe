from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, max_length=254, verbose_name="email address")
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"


class Copyright(models.Model):
    """Copyright information about a project"""
    copyright_title = models.CharField('Title', max_length=150)
    copyright_text = models.TextField('COpyright description')
    copyright_link = models.CharField(max_length=100)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.copyright_title

    def __str__(self):
        return self.copyright_title

    class Meta:
        verbose_name = 'Copyright'
        verbose_name_plural = 'Copyrights'


class Category(models.Model):
    """Category recipe"""
    title = models.CharField('Category', max_length=100, unique=True)
    description = models.TextField('Category description', null=True)
    image = models.ImageField('Image', upload_to='category/', null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Ingredient(models.Model):
    """Ingredient used in recipes"""
    title = models.CharField('Ingredient title', max_length=50, default='Title', unique=True)
    description = models.TextField('Ingredient description')
    image = models.ImageField('Image', upload_to='ingredient/', blank=True, null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipe(models.Model):
    """Recipe model"""
    recipe_title = models.CharField('Recipe title', max_length=100, unique=True)
    recipe_text = models.TextField('Recipe description')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField('Черновик', default=True)
    ingredient = models.ManyToManyField(Ingredient, verbose_name='ingredient', related_name='ingredient')
    image = models.ImageField('Image', upload_to='recipe/', blank=True, null=True)

    def __repr__(self):
        return self.recipe_title

    def __str__(self):
        return self.recipe_title

    class Meta:
        verbose_name = 'Reciep'
        verbose_name_plural = 'Recipes'


class Topic(models.Model):
    """Topic about food"""
    topic_title = models.CharField('Topic title', max_length=150, unique=True)
    topic_text = models.TextField('Topic text')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, verbose_name='recipe', blank=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField('Draft', default=False)
    image = models.ImageField('Image', upload_to='topic/', blank=True, null=True)

    def __repr__(self):
        return self.topic_title

    def __str__(self):
        return self.topic_title

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class TopicReview(models.Model):
    """Topic review showing at topic detail page"""
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=60)
    body = models.TextField('Review body', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, verbose_name='topic', related_name='review', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Topic review'
        verbose_name_plural = 'Topic reviews'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'

    def __repr__(self):
        return f'Comment by {self.name}'


class RecipeReview(models.Model):
    """Recipe review showing at topic detail page"""
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=60)
    body = models.TextField('Review body', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, verbose_name='recipe', related_name='review', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'recipe review'
        verbose_name_plural = 'recipe review'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'

    def __repr__(self):
        return f'Comment by {self.name}'


class ClickStat(models.Model):
    """Clicking statistic provided by graphql mutations and template onclick events"""
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    amount = models.PositiveIntegerField()
