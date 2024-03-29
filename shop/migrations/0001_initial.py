# Generated by Django 4.2.11 on 2024-03-28 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short but descriptive name of category', max_length=32)),
            ],
            options={
                'db_table': 'category',
                'db_table_comment': 'Categories of plants',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(help_text='Common name of the plant', max_length=128)),
                ('formal_name', models.CharField(help_text='Two term ("genus" "species") name of the plant', max_length=128)),
                ('is_poisonous', models.BooleanField(help_text='Is this plant poisonous to human')),
                ('description', models.TextField(help_text='Short info about the plant')),
                ('photo', models.ImageField(help_text='Image of the plant', upload_to='')),
                ('in_stock', models.PositiveIntegerField(default=0, help_text='How many units of the plant is currently in stock')),
                ('unit_price', models.DecimalField(decimal_places=2, help_text='Price of a single unit of the plant', max_digits=6)),
                ('category', models.ForeignKey(help_text='Category of the plant', on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'db_table': 'plant',
                'db_table_comment': 'Plants offered by the shop',
            },
        ),
    ]