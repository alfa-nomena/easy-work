from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Education, Candidate
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        for educ in tqdm(Education.objects.all(), 'Clean all educations'):
            educ.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for candidate in tqdm(Candidate.objects.filter(user__in = User.objects.filter(is_staff=False, is_active=True)), "Creating new candidates"):
            for _ in range(random.randrange(10)):
                Education.objects.create(
                    candidate = candidate,
                    institut = faker.text(20),
                    diplom = faker.text(50),
                    description = do_or_empty(faker.url),
                    start = faker.date(),
                    end = faker.date()
                )