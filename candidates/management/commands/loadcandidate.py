from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Candidate
from django.contrib.auth.models import User
from faker import Faker
import random
from mixins.routines import do_or_empty

class Command(BaseCommand):
    def clean_db(self):
        for candidate in tqdm(Candidate.objects.all(), 'Clean all Candidated'):
            candidate.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for _ in tqdm(range(random.randrange(100, 230)), "Creating new candidates"):
            while True:
                username = faker.user_name()
                if not User.objects.filter(username=username).exists():
                    break
            user = User.objects.create(
                username=username,
                password='teste',
                email= do_or_empty(faker.email),
                first_name = do_or_empty(faker.first_name),
                last_name = do_or_empty(faker.last_name)
            )
            Candidate.objects.create(
                user = user,
            )