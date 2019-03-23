from django.core.management.base import BaseCommand
from movielist.management.commands.fake_data import Populate


class Command(BaseCommand):
    help = 'Populate DB'

    def handle(self, *args, **options):
        populate = Populate()
        populate.setUp()