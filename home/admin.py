from django.contrib import admin
from .models import upcoming_Product,Best_Values,Gallery
from product.models import Category

# Register your models here.
admin.site.register(upcoming_Product)
admin.site.register(Category)
admin.site.register(Best_Values)
admin.site.register(Gallery)

