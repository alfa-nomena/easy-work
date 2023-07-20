from django.core.management.base import BaseCommand
from tqdm import tqdm
from faker import Faker
import random
from jobs.models import Job, Profil

class Command(BaseCommand):
    def clean_db(self):
        for role in tqdm(Profil.objects.all(), 'Clean all profiles'):
            role.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for job in tqdm(Job.objects.all()):
            for _ in range(random.randrange(10,156)), "Creating new profils for all jobs":
                Profil.objects.create(
                    job=job,
                    title = faker.text(50)
                )