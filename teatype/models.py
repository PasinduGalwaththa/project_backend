from django.db import models

# Create your models here.

class Teatype(models.Model):
    teatype = models.CharField(max_length=20 , null=True)
    teaprice = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return self.teatype