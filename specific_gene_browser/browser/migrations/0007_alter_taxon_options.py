# Generated by Django 3.2.5 on 2021-09-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("browser", "0006_auto_20210822_1407")]

    operations = [
        migrations.AlterModelOptions(
            name="taxon", options={"ordering": ["taxonomic_unit"]}
        )
    ]
