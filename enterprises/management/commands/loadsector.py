from django.core.management.base import BaseCommand
from tqdm import tqdm
from enterprises.models import Enterprise, Sector
from faker import Faker
import random

class Command(BaseCommand):
    def clean_db(self):
        for sector in tqdm(Sector.objects.all(), 'Clean all sectors'):
            sector.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for _ in tqdm(range(random.randrange(20, 50)), "Creating new sectors"):
            while True:
                title = faker.user_name()
                if not Sector.objects.filter(title=title).exists():
                    Sector.objects.create(
                        title=title
                    )
                    break
        for enterprise in tqdm(Enterprise.objects.all(), 'Assigning enterprise to sector'):
            for sector in Sector.objects.all().order_by('?')[:random.randrange(5)]:
                enterprise.sector_set.add(sector)
            