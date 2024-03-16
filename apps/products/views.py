from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from .models import Product
from .serializers import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from generics.utils import http_response


class ProductsView(ModelViewSet):
    # queryset = Product.objects.all()
    # serializer_class = ProductListSerializer

    @swagger_auto_schema(
        tags=["Products"],
        methods=["GET"],
        responses={
            200: ProductListResponseSerializer(many=True),
            500: "Failed to fetch values from database"
        }
    )
    @action(detail=False, methods=["GET"])
    def get_products(self, request, *args, **kwargs):

        product = Product.objects.filter(product_category="Electronics")

        return http_response(
            response_serializer_class=ProductListResponseSerializer,
            details={"count": len(product), "products": product},
        )
