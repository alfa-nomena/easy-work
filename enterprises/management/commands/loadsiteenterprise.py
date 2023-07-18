from django.core.management.base import BaseCommand
from tqdm import tqdm
from candidates.models import Site
from enterprises.models import Enterprise
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        for enterprise in tqdm(Enterprise.objects.all(), 'Clean all sites for all enterprises'):
            for site in enterprise.user.site_set.all():
                site.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for enterprise in tqdm(Enterprise.objects.filter(user__in = User.objects.filter(is_staff=False, is_active=True)), "Creating new sites for enterprises."):
                for _ in range(random.randrange(10)):
                    Site.objects.create(
                        owner = enterprise.user,
                        title = faker.text(20),
                        description = do_or_empty(faker.text,300),
                        link = faker.url()
                    )