from typing import Iterable, Optional
from django.db import models
from updates.models import updates
from teatype.models import Teatype

# Create your models here.

class payments(models.Model):
   update = models.ForeignKey(updates, on_delete=models.CASCADE)
   calculated_amount = models.FloatField(null=True)
   payment_amount = models.FloatField(null=True)
   date = models.DateField(null=True)
   teatype = models.ForeignKey(Teatype, on_delete=models.PROTECT)
   
   def __str__(self):
      return self.update.planter.first_name
   
   def save(self, *args, **kwargs):
      weight = self.update.weight
      price = self.teatype.teaprice
      
      self.calculated_amount = weight * price
      
      
      super(payments , self).save(*args, **kwargs)

   
   
