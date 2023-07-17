from django.db import models


class PeriodMixin(models.Model):
    class Meta: 
        abstract = True
    
    start = models.DateField()
    end = models.DateField()
    def period(self):
        return f"{self.start}" + (f'- {self.end}' if self.end else '')