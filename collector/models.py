from django.db import models
from planter.models import planter

# Create your models here.
class collector(models.Model):
    first_name = models.CharField(max_length=20 ,null=False)
    last_name = models.CharField(max_length=20 ,null=False)
    nic = models.CharField(max_length=4 , null=False)
    adress = models.CharField(max_length=20 , null=False)
    telephone = models.CharField(max_length=10 , null=False)
    # planter=models.ManyToManyField(planter,default=1,  )
     
    def __str__(self):
        return self.first_name
