from django.contrib import admin

from categoryproduct.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'id_channel')
    list_display_links = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
