from django.db import models
from estate.models import estate
from user.models import Customuser
from teatype.models import Teatype

# Create your models here.
class planter(models.Model):
    
    first_name = models.CharField(max_length=20 , null=False)
    last_name = models.CharField(max_length=20 ,null=False)
    address = models.CharField(max_length =50 , null=False)
    telephone = models.CharField(max_length=20,null=False)
    email= models.EmailField(max_length=50 , null=False)
    estate = models.ForeignKey(estate, on_delete=models.CASCADE,default=1 )
    nic = models.CharField(max_length=15 , null=False)
    user = models.OneToOneField(Customuser , on_delete=models.CASCADE , default=1)
    
    
   
    def __str__(self):
        return self.first_name