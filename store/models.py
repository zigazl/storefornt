from django.db import models

# Create your models here.
class Product(models.Model):
    # sku = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)  # varchar 255
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()

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
        PAYMENT_STATUS = [
            ("P", "Pending"),
            ("C", "Complete"),
            ("F", "Failed"),
        ]
        PAYMENT_STATUS_PENDING = ("P",)
        PAYMENT_STATUS_COMPLETE = ("C",)
        PAYMENT_STATUS_FAILED = "F"
