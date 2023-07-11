from django.db import models
from django.contrib.auth.models import User

from enterprises.models import Enterprise
from jobs.models import Skill

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='candidates/picture',blank=True, null=True)
    cv = models.FileField(upload_to='candidates/cv',blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    phone1 = models.CharField(max_length=20,blank=True, null=True)
    phone2 = models.CharField(max_length=20,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    title = models.CharField( max_length=100,blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    skill = models.ManyToManyField(Skill)

class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)

class Certificate(models.Model):
    institut = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    
class Site(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, blank=True, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    link = models.URLField()