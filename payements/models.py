from django.db import models
from estate.models import estate

# Create your models here.

class payments(models.Model):
   priceperkg = models.FloatField(null=False)
   amount = models.FloatField(null=False)
   estate = models.ForeignKey(estate, on_delete=models.CASCADE)
    
   def __str__(self):
      return self.priceperkg
