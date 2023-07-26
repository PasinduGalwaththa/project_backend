from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customuser(AbstractUser):
    
    Usertypes = {
        ('planter','planter'),
        ('collector','collector'),
    }
    
    usertype = models.CharField(max_length=100,choices=Usertypes,default='collector')