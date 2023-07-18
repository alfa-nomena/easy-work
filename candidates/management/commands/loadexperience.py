from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Candidate, Experience
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        for candidate in tqdm(Candidate.objects.all(), 'Clean all experiences for all candidates'):
            for exp in candidate.experience_set.all():
                exp.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for candidate in tqdm(Candidate.objects.filter(user__in = User.objects.filter(is_staff=False, is_active=True)), "Creating new experiences for candidates."):
                for _ in range(random.randrange(10)):
                    Experience.objects.create(
                        candidate = candidate,
                        title = faker.text(20),
                        description = do_or_empty(faker.text,300),
                        start = faker.date(),
                        end = faker.date()
                    )