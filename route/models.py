from django.db import models
from vehicles.models import vehicles

class Route(models.Model):
    
    routename=models.CharField(max_length=100)
    vehicles= models.ForeignKey(vehicles, on_delete=models.CASCADE)

    def __str__(self):
        return self.routename