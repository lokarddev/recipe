# Generated by Django 3.1.4 on 2021-01-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_recipe', '0007_auto_20210120_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image1',
            field=models.ImageField(null=True, upload_to='recipe/', verbose_name='Изображение1'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='recipe/', verbose_name='Изображение2'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='recipe/', verbose_name='Изображение3'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image1',
            field=models.ImageField(null=True, upload_to='topic/', verbose_name='Изображение1'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='topic/', verbose_name='Изображение2'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='topic/', verbose_name='Изображение3'),
        ),
    ]
