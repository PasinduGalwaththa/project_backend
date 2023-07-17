from django.db import models

# Create your models here.
class planter(models.Model):
    
    first_name = models.CharField(max_length=20 , null=False)
    last_name = models.CharField(max_length=20 ,null=False)
    
    address = models.CharField(max_length =50 , null=False)
    telephone = models.IntegerField(null=False)
    estate_number = models.CharField(max_length=4 , null=False)
    nic = models.CharField(max_length=15 , null=False)
    
    # def __str__(self):
    #     return self.planter_name