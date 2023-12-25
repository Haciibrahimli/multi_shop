from django.contrib import admin
from my_app.models import *

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Checkout)

