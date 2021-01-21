from django.db import models


class Copyright(models.Model):
    """Информация об авторских правах проекта"""
    copyright_title = models.CharField('Название', max_length=150)
    copyright_text = models.TextField('Описание авторских прав')
    copyright_link = models.CharField(max_length=100)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.copyright_title

    def __str__(self):
        return self.copyright_title

    class Meta:
        verbose_name = 'Авторские права'
        verbose_name_plural = 'Авторские права'


class Ingredient(models.Model):
    """Ингридиент используемый в рецептах"""
    title = models.CharField('название продукта/ингридиента', max_length=50, default='Title')
    description = models.TextField('Описание продукта/ингридиента', default='Description')
    image = models.ImageField('Изображение', upload_to='ingredient/', null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'


class Category(models.Model):
    """Категории доступные  для сортировки"""
    title = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание категории', null=True)
    image = models.ImageField('Изображение', upload_to='category/', null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipe(models.Model):
    """Рецепт блюда"""
    recipe_title = models.CharField('Название рецепта', max_length=100)
    recipe_text = models.TextField('Описание рецепта')
    image1 = models.ImageField('Изображение1', upload_to='recipe/', null=True)
    image2 = models.ImageField('Изображение2', upload_to='recipe/', null=True, blank=True)
    image3 = models.ImageField('Изображение3', upload_to='recipe/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=False)

    def __repr__(self):
        return self.recipe_title

    def __str__(self):
        return self.recipe_title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Topic(models.Model):
    """Произвольная статья по теме рецептов отображаемая на главной странице"""
    topic_title = models.CharField('Название статьи', max_length=150)
    topic_text = models.TextField('Текст статьи')
    image1 = models.ImageField('Изображение1', upload_to='topic/', null=True)
    image2 = models.ImageField('Изображение2', upload_to='topic/', null=True, blank=True)
    image3 = models.ImageField('Изображение3', upload_to='topic/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, verbose_name='рецепт', blank=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=False)

    def __repr__(self):
        return self.topic_title

    def __str__(self):
        return self.topic_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
