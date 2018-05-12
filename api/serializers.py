from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'name', 'store_name', 'date_created')
