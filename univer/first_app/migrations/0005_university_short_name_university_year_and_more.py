# Generated by Django 5.0.4 on 2024-04-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_remove_product_cost_product_birth_product_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='short_name',
            field=models.CharField(default=0, max_length=10, verbose_name='Сокращенное название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='year',
            field=models.CharField(default=0, max_length=10, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]