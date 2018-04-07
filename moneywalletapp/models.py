# noinspection PyUnresolvedReferences
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    Custdetail=models.OneToOneField(User,on_delete=models.CASCADE)
    walletbalance=models.DecimalField(max_digits=10,decimal_places=2,default=100.00)



