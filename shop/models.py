from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'category'
        db_table_comment = 'Categories of plants'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=32, help_text='Short but descriptive name of category')

    def __str__(self):
        return self.name


class Plant(models.Model):
    class Meta:
        db_table = 'plant'
        db_table_comment = 'Plants offered by the shop'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    common_name = models.CharField(max_length=128, help_text='Common name of the plant')
    formal_name = models.CharField(max_length=128, help_text='Two term ("genus" "species") name of the plant')
    is_poisonous = models.BooleanField(help_text='Is this plant poisonous to human')
    description = models.TextField(help_text='Short info about the plant')
    photo = models.ImageField(help_text='Image of the plant')
    in_stock = models.PositiveIntegerField(default=0, help_text='How many units of the plant is currently in stock')
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, help_text='Price of a single unit of the plant')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, help_text='Category of the plant')

    def __str__(self):
        return f'{self.common_name} ({self.formal_name})'
