# Generated by Django 3.1.4 on 2021-01-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_recipe', '0005_auto_20210129_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(related_name='ingredient', to='main_recipe.Ingredient', verbose_name='ингредиенты'),
        ),
    ]
