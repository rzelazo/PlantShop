# Generated by Django 4.2.11 on 2024-03-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'Plant', 'verbose_name_plural': 'Plants'},
        ),
    ]
