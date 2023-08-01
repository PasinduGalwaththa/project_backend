from typing import Iterable, Optional
from django.db import models
from updates.models import updates
from teatype.models import Teatype
from datetime import timedelta
from planter.models import planter

# Create your models here.

class payments(models.Model):
    calculated_amount = models.FloatField(null=True, blank=True)
    payment_amount = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True)
    gross_weight = models.FloatField(null=True, blank=True)
    planter = models.ForeignKey(planter, on_delete=models.PROTECT)
    got_paid = models.BooleanField(default=False)
    transferred = models.BooleanField(default=False)

    def __str__(self):
        return self.calculated_amount.__str__()

    def save(self, *args, **kwargs):
        thirty_days_ago = self.date - timedelta(days=30)

        print(self.planter.estate.teatype.teatype)

        relevant_updates = updates.objects.filter(
            planter=self.planter,
            collected_date__gte=thirty_days_ago,
            collected_date__lte=self.date
        )

        for update in relevant_updates:
            update.got_paid = True
            update.save()

        calculated_weight = sum(update.weight for update in relevant_updates)
        self.gross_weight = calculated_weight
        self.calculated_amount = calculated_weight * self.planter.estate.teatype.teaprice

        # Check if the current gross_weight is different from the previous one
        if self.pk:  # If the instance has a primary key, it means it's an existing record
            previous_record = payments.objects.filter(pk=self.pk).first()
            if previous_record and self.gross_weight == previous_record.gross_weight:
                return  # If the gross_weight is the same, don't save the newer record

        super(payments, self).save(*args, **kwargs)
