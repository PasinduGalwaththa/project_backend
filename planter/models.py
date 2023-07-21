from django.db import models
from estate.models import estate

# Create your models here.
class planter(models.Model):
    
    first_name = models.CharField(max_length=20 , null=False)
    last_name = models.CharField(max_length=20 ,null=False)
    
    address = models.CharField(max_length =50 , null=False)
    telephone = models.IntegerField(null=False)
    estate = models.ForeignKey(estate,default=1,  on_delete=models.CASCADE)
    nic = models.CharField(max_length=15 , null=False)
    
    # def __str__(self):
    #     return self.first_name