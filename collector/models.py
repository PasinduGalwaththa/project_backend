from django.db import models
from user.models import Customuser

# Create your models here.
class collector(models.Model):
    first_name = models.CharField(max_length=20 ,null=False)
    last_name = models.CharField(max_length=20 ,null=False)
    nic = models.CharField(max_length=12 , null=False)
    address = models.CharField(max_length=100 , null=False)
    email= models.EmailField(max_length=50 , null=False)
    telephone = models.CharField(max_length=10 , null=False)
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE)
   
     
    def __str__(self):
        return self.first_name
