import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from common.models import Region


class Command(BaseCommand):
    help = "Uploads the regions"

    def handle(self, *args, **options):
        try:
            Region.objects.all().delete()  # delete all regions
            # read csv file
            dfs = pd.read_csv("common/management/data/regions.csv")
            for index, row in dfs.iterrows():
                name = row["name_uz"]
                Region.objects.create(name=name)

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created region {name}")
                )
            self.stdout.write(self.style.SUCCESS("Successfully uploaded the regions"))
        except Exception as e:
            raise CommandError(f"Failed to upload the regions: {e}")
