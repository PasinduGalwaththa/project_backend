from django.db import models
from vehicles.models import vehicles
from collector.models import collector

class Route(models.Model):
    
    routename=models.CharField(max_length=100)
    vehicles= models.ForeignKey(vehicles, on_delete=models.CASCADE)

    def __str__(self):
        return self.routename
    

class RouteDetails(models.Model):
    
    days = {
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    }
    
    route=models.ForeignKey(Route, on_delete=models.CASCADE)
    collector = models.ForeignKey(collector, on_delete=models.CASCADE)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    day = models.CharField(max_length=20 , choices=days)
    
    def __str__(self):
        return self.id
    