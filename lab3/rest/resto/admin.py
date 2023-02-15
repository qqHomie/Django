from django.contrib import admin
from .models import Restaurant, MenuCategory, Dish, Order
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(Dish)
admin.site.register(Order)
