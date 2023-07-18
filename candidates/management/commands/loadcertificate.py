from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Certificate, Candidate
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        for cert in tqdm(Certificate.objects.all(), 'Clean all Certifications'):
            cert.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for candidate in tqdm(Candidate.objects.filter(user__in = User.objects.filter(is_staff=False, is_active=True)), "Creating new Certifications"):
            for _ in range(random.randrange(5)):
                Certificate.objects.create(
                    candidate = candidate,
                    institut = faker.text(20),
                    title = faker.text(50),
                    description = do_or_empty(faker.text, 100),
                    obtention_date = faker.date(),
                    link = do_or_empty(faker.url)
                )