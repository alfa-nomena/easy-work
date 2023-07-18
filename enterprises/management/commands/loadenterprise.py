from django.core.management.base import BaseCommand
from tqdm import tqdm
from enterprises.models import Enterprise, SIZES
from faker import Faker
import random
from mixins.routines import do_or_empty
from django.contrib.auth.models import User

class Command(BaseCommand):
    def clean_db(self):
        print(Enterprise.objects.all())
        for enterprise in tqdm(Enterprise.objects.all(), 'Clean all Enterprises'):
            enterprise.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for _ in tqdm(range(random.randrange(20, 50)), "Creating new Enterprise"):
            while True:
                username = faker.user_name()
                if not User.objects.filter(username=username).exists():
                    break
            user = User.objects.create(
                username=username,
                password='teste',
                email= do_or_empty(faker.email),
                first_name = faker.first_name(),
                last_name = faker.last_name()
            )
            Enterprise.objects.create(
                user = user,
                title = faker.text(20),
                description = do_or_empty(faker.text, 200),
                size = random.choice(SIZES)[0],
                address = faker.address(),
                date_founded = faker.date()
            )