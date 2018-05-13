from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'name', 'store_name', 'price', 'date_created')

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    store_name = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
