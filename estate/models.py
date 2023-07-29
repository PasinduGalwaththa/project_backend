from django.db import models
from teatype.models import Teatype
# Create your models here.


class estate(models.Model):
    
    estatename = models.CharField(max_length=20 , null=True)
    teatype = models.ForeignKey(Teatype, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.estatename
