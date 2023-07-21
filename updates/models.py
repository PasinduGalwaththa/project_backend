from django.db import models
from planter.models import planter

from set_arrivals.models import SetArrivals


# Create your models here.
class updates(models.Model):
    
    # estate_number = models.CharField(max_length=4 , null=False)
    # planter_name = models.CharField(max_length=20 ,null=False)
    planter = models.ForeignKey(planter, on_delete=models.CASCADE)
    # collector=models.ForeignKey(collector, on_delete=models.CASCADE)
    # SetArrivals=models.ForeignKey(SetArrivals, on_delete=models.CASCADE)
    
    collected_date = models.DateField(null=False)
    weight = models.FloatField(null=False)
    
    
    def __str__(self):
        return self.planter.first_name