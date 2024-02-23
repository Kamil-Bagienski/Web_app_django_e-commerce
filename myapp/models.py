from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

class Order(models.Model):
    PAYMENT_METHODS = (
        ('card', 'Karta'),
        ('cod', 'Pobranie'),
        ('paypal', 'PayPal'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)  
    amount = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.product:
            self.product_name = self.product.name
        super(Order, self).save(*args, **kwargs)
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField()
