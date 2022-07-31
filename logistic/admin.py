from django.contrib import admin

# Register your models here.
from logistic.models import StockProduct, Stock, Product


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stock)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']


# class RelationshipInline(admin.TabularInline):
#     model = StockProduct


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']
    # inlines = [RelationshipInline, ]
