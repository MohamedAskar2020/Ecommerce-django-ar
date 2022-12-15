from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.register(Variant)
admin.site.register(Brand)
admin.site.register(Comment)
