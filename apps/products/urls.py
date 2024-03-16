from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ProductsView

urlpatterns = [
    path("products/", ProductsView.as_view({"get": "get_products"}), name="get-product")
]
