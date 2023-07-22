from django.db import models
from collector.models import collector

from planter.models import planter






# Create your models here.
class updates(models.Model):
    
    # estate_number = models.CharField(max_length=4 , null=False)
    # planter_name = models.CharField(max_length=20 ,null=False)
   
    collector=models.ForeignKey(collector,default=1, on_delete=models.CASCADE)
    planter = models.ForeignKey(planter, on_delete=models.CASCADE)
    # collector=models.ForeignKey(collector, on_delete=models.CASCADE)
    # SetArrivals=models.ForeignKey(SetArrivals, on_delete=models.CASCADE)
    
    collected_date = models.DateField(null=False)
    weight = models.FloatField(null=False)
    
    
    def __str__(self):
        return self.planter.first_name