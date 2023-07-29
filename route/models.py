from django.db import models

class Route(models.Model):
    DAY_CHOICES = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='Sunday')
    started_time = models.TimeField(null=True, blank=True)
    ended_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Route: {self.day}, Started Time: {self.started_time}, Ended Time: {self.ended_time}"