from django.db import models

# Create your models here.
class updates(models.Model):
    
    estate_number = models.CharField(max_length=4 , null=False)
    planter_name = models.CharField(max_length=20 ,null=False)
    collected_date = models.DateField(null=False)
    weight = models.FloatField(null=False)
    
    def __str__(self):
        return self.planter_name