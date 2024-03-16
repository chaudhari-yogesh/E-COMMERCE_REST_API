from django.contrib import admin

from .models import *


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'product_desc', 'product_price', 'product_category', 'created_at',
                    'modified_at']
