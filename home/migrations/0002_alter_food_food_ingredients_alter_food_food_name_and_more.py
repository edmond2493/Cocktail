# Generated by Django 4.1.6 on 2023-02-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_ingredients',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_steps',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_steps',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_title',
            field=models.CharField(max_length=100),
        ),
    ]