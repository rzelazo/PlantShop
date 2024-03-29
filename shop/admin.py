from django.contrib.admin import ModelAdmin, register

from shop.models import Category, Plant


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name']


@register(Plant)
class PlantAdmin(ModelAdmin):
    list_display = ['common_name', 'unit_price', 'in_stock', 'category']
    pass

