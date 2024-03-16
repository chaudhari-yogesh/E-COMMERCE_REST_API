from rest_framework import serializers
from .models import Product
from generics.serializers import CommonSerializerResponseView


class ProductListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product_title = serializers.CharField()
    product_desc = serializers.CharField()
    product_price = serializers.IntegerField()
    product_category = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductListResponse(serializers.Serializer):
    count = serializers.IntegerField()
    products = ProductListSerializer(many=True)


class ProductListResponseSerializer(CommonSerializerResponseView):
    details = ProductListResponse()

    class Meta:
        ref_name = "ProductListResponseSerializer"
