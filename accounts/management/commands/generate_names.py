from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import PredefinedN
import random
import uuid


class Command(BaseCommand):
    help = 'Generate random names and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of names to generate')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']

        def generate_abstract_name():
            parts = [
                #fake.first_name(),
                fake.color_name(),
                fake.word(),
                #fake.city()
                #fake.animal()
            ]
            random.shuffle(parts)
            na = f"{''.join(parts)}_{str(uuid.uuid4().int)[:3]}"
            return na

        for _ in range(count):
            unique = False
            while not unique:
                name = generate_abstract_name()
                if not PredefinedN.objects.filter(name=name).exists():
                    PredefinedN.objects.create(name=name)
                    unique = True
                    self.stdout.write(self.style.SUCCESS(f'Successfully created name: {name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} unique names'))
