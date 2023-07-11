from django.db import models

from enterprises.models import Enterprise

TYPES = [
    ('ft', 'Full time'),
    ('pt', 'Part time')
]
CONTRACTS = [(contract, contract) for contract in ['CDI', 'CDD']]
EXPERIENCES = [
    ('fresher', '< 1 years'),
    ('junior', '1-2 years'),
    ('confirmed', '3-5 years'),
    ('senior', '6-10 years'),
    ('expert', '>10 years')
]


class Detail(models.Model):
    class Meta:
        abstract=True
        
    title = models.CharField(max_length=50)
    
class Role(Detail):
    pass
class Profil(Detail):
    pass
class Skill(Detail):
    pass

class Job(models.Model):
    title = models.CharField(max_length=50)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, blank=True, null=True)
    date_posted = models.DateField(auto_now=True)
    date_last_modified = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=TYPES, default='ft')
    address = models.CharField(max_length=50,blank=True, null=True)
    contract = models.CharField(max_length=50, choices=TYPES, default='CDI')
    experience = models.CharField(max_length=50, choices=EXPERIENCES)
    skill = models.ManyToManyField(Skill)
    profil = models.ManyToManyField(Profil)
    role = models.ManyToManyField(Role)