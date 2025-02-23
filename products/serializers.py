from dataclasses import field
import re
from wsgiref.validate import validator
from rest_framework import serializers
from . import validators

from products.models import Maker, Product, ProductCategory


class ProductCategoryInlineSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)


class ProductCategorySerializer(serializers.ModelSerializer):

    children_categories = ProductCategoryInlineSerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = "__all__"
        # depth = 1


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"
        depth = 1


class ProductInlineSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    title = serializers.CharField(validators=[validators.unique_title_validator])
    variation_product = serializers.SerializerMethodField(read_only=True)
    maker_products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

    def get_variation_product(self, obj):
        qs = Product.objects.filter(id__in=obj.variation_product_ids).first()
        return ProductInlineSerializer(qs, many=False).data

    def get_maker_products(self, obj):
        if obj.maker is None:
            return []
        qs = obj.maker.products.all().order_by("-id")[:1]
        return ProductInlineSerializer(qs, many=True).data
