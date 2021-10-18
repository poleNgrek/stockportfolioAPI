from __future__ import with_statement
import sys
from django.core.management.base import BaseCommand
import json
from trading.models import Instruments

class Command(BaseCommand):
    help = 'Load JSON instrument data'

    # def add_arguments(self, parser):
    #     parser.add_argument('instrument_file', type=str, help='A json data file for instruments')

    def handle(self, *args, **options):
        if Instruments.objects.all().exists:
            pass
        else:
            try:
                with open("instruments_data.json") as f:
                    data = json.load(f)
                for instrument in data:
                    Instruments.objects.create(**instrument)
                self.stdout.write(self.style.SUCCESS('The data has been imported successfully.'))
            except EnvironmentError as e:
                self.stdout.write(self.style.ERROR(e))
                self.stdout.write(self.style.ERROR(sys.exc_info()[0]))
