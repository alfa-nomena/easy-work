from django.core.management.base import BaseCommand
from tqdm import tqdm
from faker import Faker
import random
from jobs.models import Job, Role

class Command(BaseCommand):
    def clean_db(self):
        for role in tqdm(Role.objects.all(), 'Clean all roles'):
            role.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for job in tqdm(Job.objects.all()):
            for _ in range(random.randrange(5,10)), "Creating new roles for all jobs":
                Role.objects.create(
                    job=job,
                    title = faker.text(50)
                )