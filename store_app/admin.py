from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category_Model)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Auto-fill slug based on name
    list_display = ("name", "slug", "status", "trending", "created_at")

@admin.register(Product_Model)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Pre-fills slug based on name
    list_display = ("name", "slug", "category", "created_at")
    
admin.site.register(Cart_Model)