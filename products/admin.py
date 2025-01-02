from django.contrib import admin

from django.contrib import admin
from .models import Product, ArtCollection

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'art_collection',
        'price',
        'upvotes',
        'downvotes',
        'image',
    )

    ordering = ('sku',)

class ArtCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(ArtCollection, ArtCollectionAdmin)
