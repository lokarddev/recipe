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


class Recipe(models.Model):
    """Рецепт блюда"""
    recipe_title = models.CharField('Название рецепта', max_length=100)
    recipe_text = models.TextField('Описание рецепта')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=True)
    ingredient = models.ManyToManyField(Ingredient, verbose_name='рецепт', related_name='ingridient')

    def get_main_image(self):
        """Главное изображение для карточки рецепта"""
        return self.recipeimage_set.all()[0]

    def get_queryset_image(self):
        """Полный набор изображений рецепта"""
        return self.recipeimage_set.all()

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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, verbose_name='рецепт', blank=True)
    url = models.SlugField(max_length=100, unique=True, null=True)
    draft = models.BooleanField('Черновик', default=False)

    def get_main_image(self):
        """Главное изображение для карточки статьи"""
        return self.topicimage_set.all()[0]

    def get_queryset_image(self):
        """Полный набор изображений статьи"""
        return self.topicimage_set.all()

    def __repr__(self):
        return self.topic_title

    def __str__(self):
        return self.topic_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class TopicImage(models.Model):
    """Изображения статьи"""
    image = models.ImageField('Изображение', upload_to='topic/', null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.topic.topic_title}' + ' ' + f'{self.id}'


class RecipeImage(models.Model):
    """Изображения рецепта"""
    image = models.ImageField('Изображение', upload_to='recipe/', null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.recipe.recipe_title}' + ' ' + f'{self.id}'


class TopicReview(models.Model):
    """Отзыв о статье"""
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=60)
    body = models.TextField('Тело отзыва', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, verbose_name='статья', related_name='review', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
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
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'

    def __repr__(self):
        return f'Comment by {self.name}'
