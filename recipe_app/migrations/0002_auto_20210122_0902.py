# Generated by Django 3.1.4 on 2021-01-22 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeimage',
            old_name='topic',
            new_name='recipe',
        ),
    ]