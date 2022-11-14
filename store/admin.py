from django.contrib import admin
from  .models import Product, Category, Customer


admin.site.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id','firstname','lastname','phoneno','email','password']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','description','image']

