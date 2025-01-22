from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
   

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    datetime = models.DateTimeField("order placed at", auto_now_add=True)
    
    def __str__(self):
        return f'Order {self.id} - {self.customer.name} {self.datetime}'

    def calculate_total(self):
        order_items = OrderItem.objects.filter(order=self)
        return sum(item.price * item.quantity for item in order_items)

    def get_items(self):
        # order_items = OrderItem.objects.filter(orderID=self)
        order_items = OrderItem.objects.filter(orderID=self)
        # for item in order_items:
        #     return f"{item.itemID.name} x {item.quantity}"
        return ", ".join(item.name for item in order_items)


    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        self.items = self.get_items()
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
        
    def __str__(self):
        return f'Order Item {self.id} - {self.orderID.datetime} (Order {self.orderID.id})'

    def get_price():
        price = Item.objects.get(itemID=self).price
        return price

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.itemID.price
        super().save(*args, **kwargs)
        