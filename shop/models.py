from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="Phone number must be in the format: '+254712345678'."
            )
        ],
        help_text="Include country code, e.g., +254712345678"
    )
    # Bussiness Address: You can use one feild or split into multiple (street, city, etc.)
    business_address = models.TextField(
        help_text="Enter full business address"
    )

    def __str__(self):
        return self.name


class SellModel(models.Model):
    product = models.CharField(max_length=60)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    unit = models.IntegerField()
    description = models.TextField()
