from rest_framework import serializers
from pprint import pprint

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        positions = positions[0]

        # pprint(validated_data)
        # print(positions['stock'])

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        stockproduct = StockProduct.objects.update_or_create(validated_data)
        # stocks_products = StockProduct.objects.create(stock=positions['stock'], product=positions['product'],
        #     quantity=positions['quantity'], price=positions['price'])

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        positions = positions[0]

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        # positions, stocks_products = StockProduct.objects.update_or_create(
        #     stock=positions['stock'], product=positions['product'],
        #     quantity=positions['quantity'], price=positions['price'])

        return stock

# {
#     "address": "Таганская 2",
#     "positions": [
#             {
#                 "id": 1,
#                 "stock": 1,
#                 "product": 3,
#                 "quantity": 8,
#                 "price": "0.20"
#             }
# ]
# }
