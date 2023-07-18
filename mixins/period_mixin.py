from django.db import models
from django.utils import timezone

class PeriodMixin(models.Model):
    class Meta: 
        abstract = True
    
    start = models.DateField()
    end = models.DateField(default=timezone.now, blank=True)
    def period(self):
        return f"{self.start} to {self.end}"