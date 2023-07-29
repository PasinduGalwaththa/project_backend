from django.db import models
from collector.models import collector
from route.models import Route






class vehicles(models.Model):
    vehiclenumber = models.CharField(max_length=20, null=False)
    drivername = models.CharField(max_length=20, null=False)
    routename = models.CharField(max_length=20, null=False)
    collector = models.OneToOneField(collector, on_delete=models.CASCADE)
    routes = models.ManyToManyField(Route)
    

    def __str__(self):
        return f"{self.vehiclenumber} - Driver: {self.drivername},routename:{self.routename}, Collector: {self.collector}, routes: {self.routes}"
    