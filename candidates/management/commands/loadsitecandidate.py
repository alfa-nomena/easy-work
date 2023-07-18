from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Candidate, Site
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        for candidate in tqdm(Candidate.objects.all(), 'Clean all sites for all candidates'):
            for site in candidate.user.site_set.all():
                site.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for candidate in tqdm(Candidate.objects.filter(user__in = User.objects.filter(is_staff=False, is_active=True)), "Creating new sites for candidates."):
                for _ in range(random.randrange(10)):
                    Site.objects.create(
                        owner = candidate.user,
                        title = faker.text(20),
                        description = do_or_empty(faker.text,300),
                        link = faker.url()
                    )