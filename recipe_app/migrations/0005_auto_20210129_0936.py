# Generated by Django 3.1.4 on 2021-01-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0004_recipereview_topicreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Черновик'),
        ),
    ]