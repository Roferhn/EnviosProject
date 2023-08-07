from django.db import models

# Create your models here.

# ---User Models--#
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField(null=False) #Investigar e implementar hashing
    phone = models.CharField(max_length=8)
    locker = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    
    USER_TYPES = (
        ('admin', 'Admin'),
        ('op','Operator'),
        ('client','Client')
    )
    type = models.CharField(max_length=10, choices=USER_TYPES)


# ---Package Models---#
class Package(models.Model):
    tracking_num = models.TextField()
    locker = models.IntegerField()
    weight = models.DecimalField()
    reception_date = models.DateField()
    packaged_date = models.DateField()

# --- Shipping Models---#
class Shipping(models.Model):
    delicery_date = models.DateField()
    updated_date = models.DateField()

    SHIPPING_STATUS =(
        ('1','')
    )