from tkinter import CASCADE
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.forms import ImageField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserMaster(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=1000)
    otp = models.IntegerField()
    Is_active = models.BooleanField(default=True)
    Is_verified = models.BooleanField(default=False)
    Is_created = models.BooleanField(default=True)
    Is_modified = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    pincode = models.CharField(max_length=20)
    near = models.CharField(max_length=200)


class Food(models.Model):
    foodname=models.CharField(max_length=200)
    foodtype=models.CharField(max_length=200)
    foodprice=models.IntegerField()
    offerprice=models.IntegerField(default=0)
    offer=models.IntegerField(default=0)
    foodpic = models.ImageField(upload_to="app/foodimg")

class Order(models.Model):
    orderid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    foodid = models.ForeignKey(Food,on_delete=models.CASCADE, blank=True, null=True)
    offerprice = models.IntegerField(default=0)
    totalAmount = models.IntegerField(default=0)
    deladdress = models.CharField(max_length=250)
    delpincode = models.CharField(max_length=50)
    delnear = models.CharField(max_length=200)
    delcontact = models.CharField(max_length=20)
    delcharge = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    paymentmethod = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=100, default=0)
    paid = models.BooleanField(default=False)

class Cart(models.Model):
    cust_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_id=models.ForeignKey(Food, on_delete=models.CASCADE)


class ReviewTab(models.Model):
    cust_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating=models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    description=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)


    
