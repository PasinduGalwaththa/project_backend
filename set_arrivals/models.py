from django.db import models

# Create your models here.
class SetArrivals(models.Model):
    DAY=(
        ('Monday','monday'),
        ('Tuesday','tuesday'),
        ('Wednesday','wednesday'),
        ('Thursday','thursday'),
        ('Friday','friday'),
        ('Saturday','saturday'),
        ('Sunday','sunday')	
    )
    id=models.AutoField(primary_key=True)
    collectionpointname=models.CharField(max_length=30)
    # collectionpoint=models.CharField(max_length=30)
    arrivaltime=models.CharField(max_length=30)
    day=models.CharField(max_length=30,choices=DAY)
    
    
    def __str__(self):
        return self.collectionpointname
          
