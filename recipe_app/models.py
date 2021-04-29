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


class Category(models.Model):
    """Категории доступные  для сортировки"""
    title = models.CharField('Категория', max_length=100, unique=True)
    description = models.TextField('Описание категории', null=True)
    image = models.ImageField('Изображение', upload_to='category/', null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ingredient(models.Model):
    """Ингридиент используемый в рецептах"""
    title = models.CharField('Название продукта/ингридиента', max_length=50, default='Title', unique=True)
    description = models.TextField('Описание продукта/ингридиента', default='Description')
    image = models.ImageField('Изображение', upload_to='ingredient/', null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'


class Recipe(models.Model):
    """Рецепт блюда"""
    recipe_title = models.CharField('Название рецепта', max_length=100, unique=True)
    recipe_text = models.TextField('Описание рецепта')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=True)
    ingredient = models.ManyToManyField(Ingredient, verbose_name='ингредиенты', related_name='ingredient')
    image = models.ManyToManyField('RecipeImage', verbose_name='images', related_name='recipe_image')

    def __repr__(self):
        return self.recipe_title

    def __str__(self):
        return self.recipe_title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Topic(models.Model):
    """Произвольная статья по теме рецептов отображаемая на главной странице"""
    topic_title = models.CharField('Название статьи', max_length=150, unique=True)
    topic_text = models.TextField('Текст статьи')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, verbose_name='рецепт', blank=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=False)
    image = models.ManyToManyField('TopicImage', verbose_name='images', related_name='topic_image')

    def __repr__(self):
        return self.topic_title

    def __str__(self):
        return self.topic_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class TopicImage(models.Model):
    """Изображения статьи"""
    title = models.CharField('Image title', max_length=50, default='title')
    image = models.ImageField('Изображение', upload_to='topic/', null=True)

    def __str__(self):
        return f'{self.title}'


class RecipeImage(models.Model):
    """Изображения рецепта"""
    title = models.CharField('Image title', max_length=50, default='title')
    image = models.ImageField('Изображение', upload_to='recipe/', null=True)

    def __str__(self):
        return f'{self.title}'


class TopicReview(models.Model):
    """Отзыв о статье"""
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=60)
    body = models.TextField('Тело отзыва', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, verbose_name='статья', related_name='review', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'отзыв о статье'
        verbose_name_plural = 'отзывы о статье'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'

    def __repr__(self):
        return f'Comment by {self.name}'


class RecipeReview(models.Model):
    """Отзыв о рецепте"""
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=60)
    body = models.TextField('Тело отзыва', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, verbose_name='рецепт', related_name='review', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'отзыв о рецепте'
        verbose_name_plural = 'отзывы о рецепте'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'

    def __repr__(self):
        return f'Comment by {self.name}'
