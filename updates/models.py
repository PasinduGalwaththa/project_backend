from django.db import models
from collector.models import collector
from planter.models import planter
from estate.models import estate

class updates(models.Model):
    collector = models.ForeignKey(collector, default=1, on_delete=models.CASCADE)
    planter = models.ForeignKey(planter, on_delete=models.CASCADE)
    estate = models.ForeignKey(estate, on_delete=models.CASCADE)
    got_paid = models.BooleanField(default=False)
    collected_date = models.DateField(null=False)
    weight = models.FloatField(null=False)
    
    def __str__(self):
        return self.planter.first_name + " " + self.planter.last_name + " " + str(self.collected_date) + " " + str(self.weight)
