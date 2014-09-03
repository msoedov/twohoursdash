import sys

from django.core.management.base import BaseCommand

from ...factories import UserFactory


class Command(BaseCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        sys.stdout.write('Starting fill db\r\n')

        UserFactory.create_batch(100)

        sys.stdout.write('Completed fill db\r\n')
