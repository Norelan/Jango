# Generated by Django 5.0.4 on 2024-04-12 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_university_alter_product_cost_alter_product_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='manufacturer',
            new_name='univer',
        ),
    ]
