from django.contrib import admin
from webapp.models import Product, Review
# Register your models here.


class PRODUCT_ADMIN(admin.ModelAdmin):
    list_display = ['name']


class REVIEW_ADMIN(admin.ModelAdmin):
    list_display = ['author']


admin.site.register(Product, PRODUCT_ADMIN)
admin.site.register(Review, REVIEW_ADMIN)
