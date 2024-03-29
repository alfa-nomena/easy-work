from django.core.management.base import BaseCommand
from tqdm import tqdm
from faker import Faker
import random
from enterprises.models import Enterprise
from mixins.routines import do_or_empty
from jobs.models import Job, TYPES, CONTRACTS, EXPERIENCES_PERIODS

class Command(BaseCommand):
    def clean_db(self):
        for job in tqdm(Job.objects.all(), 'Clean all jobs'):
            job.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for enterprise in tqdm(Enterprise.objects.all()):
            for _ in range(random.randrange(20)), "Creating new jobs":
                Job.objects.create(
                    title = faker.text(50),
                    enterprise = enterprise,
                    type_value = random.choice(TYPES)[0],
                    address = faker.address(),
                    contract_value = random.choice(CONTRACTS)[0],
                    experience_value = random.choice(EXPERIENCES_PERIODS)[0]
                )