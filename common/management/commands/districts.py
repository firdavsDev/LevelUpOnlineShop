import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from common.models import Region, District


class Command(BaseCommand):
    help = "Uploads the regions"

    def handle(self, *args, **options):
        try:
            District.objects.all().delete()  # delete all regions
            dfs1 = pd.read_csv("common/management/data/regions.csv")
            regions = {}
            for index, row in dfs1.iterrows():
                id = row["id"]
                name = row["name_uz"]
                regions[id]=name

            # read csv file
            dfs = pd.read_csv("common/management/data/districts.csv")
            for index, row in dfs.iterrows():
                id = row["region_id"]
                region_name = regions[id]
                name = row["name_uz"]
                region_obj = Region.objects.get(name=region_name)
                District.objects.create(name=name, region=region_obj)

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created region {name}")
                )
            self.stdout.write(self.style.SUCCESS("Successfully uploaded the regions"))
        except Exception as e:
            raise CommandError(f"Failed to upload the regions: {e}")
