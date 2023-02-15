from django.db import models

# Create your models here.
# 1 - Restaurant(name, address)
# 2 - MenuCategory(name, restaurant)
# 3 - Dish(name, category, price)
# 4 - Order(client_name, date_ordered, restaurant, dish)

class Restaurant(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

class Dish(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(to=MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    client_name = models.CharField(max_length=128, unique=True)
    date_ordered = models.DateTimeField()
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(to=Dish, on_delete=models.CASCADE)