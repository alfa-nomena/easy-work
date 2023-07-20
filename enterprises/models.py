from django.db import models
from django.contrib.auth.models import User
from mixins.responsible import HasResponsible

# from candidates.models import Candidate

SIZES = [
    ('small','<20'),
    ('medium', '20-100'),
    ('big', '101-500'),
    ('large', '501>2000'),
    ('enormous', '>2000')
]

class Enterprise(models.Model, HasResponsible):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='candidates/picture',blank=True, null=True)
    title = models.CharField( max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=50, choices=SIZES)
    address = models.CharField(max_length=50,blank=True, null=True)
    date_founded = models.DateField()
    
    @property
    def site_set(self):
        return self.user.site_set.all()
    
    def __str__(self):
        return f"{self.name} - {self.title}"