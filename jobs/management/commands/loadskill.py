from django.core.management.base import BaseCommand
from tqdm import tqdm
from faker import Faker
import random
from jobs.models import Job, Skill

class Command(BaseCommand):
    def clean_db(self):
        for skill in tqdm(Skill.objects.all(), 'Clean all skills'):
            skill.delete()
                        
    def handle(self, *args, **kwargs):
        self.clean_db()
        faker = Faker()
        for _ in tqdm(range(random.randrange(100,200)), "Creating new skills"):
            Skill.objects.create(
                title = faker.text(15)
            )
        skills = Skill.objects.all().order_by('?')
        for job in tqdm(Job.objects.all(), "Affecting random skill for all jobs"):
            for _ in range(random.randrange(5,10)):
                job.skill_set.add(random.choice(skills))