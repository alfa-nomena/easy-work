from django.db import models
from candidates.models import Candidate
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
    ('expert', '>10 years'),
    ('any', 'Any')
]



class Job(models.Model):
    title = models.CharField(max_length=50)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now=True)
    date_last_modified = models.DateField(auto_now_add=True)
    type_value = models.CharField(max_length=50, choices=TYPES, default='ft')
    address = models.CharField(max_length=50,blank=True, null=True)
    contract_value = models.CharField(max_length=50, choices=CONTRACTS, default='CDI')
    experience_value = models.CharField(max_length=50, choices=EXPERIENCES, default='any')
    
    @property
    def contract(self):
        return self.get_contract_value_display()
    
    @property
    def experience(self):
        return self.get_experience_value_display()
    
    @property
    def type(self):
        return self.get_type_value_display()
    @property
    def enterprise_display(self):
        return self.enterprise
class Skill(models.Model):
    title = models.CharField(max_length=50)
    candidates = models.ManyToManyField(Candidate)
    jobs = models.ManyToManyField(Job)
    
class Detail(models.Model):
    class Meta:
        abstract=True
    title = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
class Role(Detail):
    pass
class Profil(Detail):
    pass
