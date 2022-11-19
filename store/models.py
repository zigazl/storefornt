from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField("Product")


class Product(models.Model):
    # sku = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)  # varchar 255
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    order = models.ManyToManyField("Order")
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        ("G", "Gold"),
        ("S", "Silver"),
        ("B", "Bronze"),
    ]
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    PAYMENT_STATUS = [
        ("P", "Pending"),
        ("C", "Complete"),
        ("F", "Failed"),
    ]
    PAYMENT_STATUS_PENDING = ("P",)
    PAYMENT_STATUS_COMPLETE = ("C",)
    PAYMENT_STATUS_FAILED = "F"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
