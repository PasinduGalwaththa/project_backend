from django.db import models
# Create your models here.

class estate(models.Model):
    estatename = models.CharField(max_length=20 , null=False)
    teatype = models.CharField(max_length=20 , null=False)
    estatenumber = models.CharField(max_length=20 , default=1,null=False)
    #collector = models.ForeignKey(collector, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.estatename
