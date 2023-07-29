from django.db import models
from collector.models import collector
from planter.models import planter
from estate.models import estate

class updates(models.Model):
    collector = models.ForeignKey(collector, default=1, on_delete=models.CASCADE)
    planter = models.ForeignKey(planter, on_delete=models.CASCADE)
    estate = models.ForeignKey(estate, on_delete=models.CASCADE)
    
    collected_date = models.DateField(null=False)
    weight = models.FloatField(null=False)
    
    def __str__(self):
        return self.planter.first_name
