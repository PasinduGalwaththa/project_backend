from django.db import models
from collector.models import collector

# Create your models here.

class vehicles(models.Model):
    vehiclenumber = models.CharField(max_length=20, null=False)
    drivername = models.CharField(max_length=20, null=False)
    routename = models.CharField(max_length=20,null=False)
    collector = models.OneToOneField(collector, on_delete=models.CASCADE)
   
    
    # def __str__(self):
    #     return self.vehicle_id