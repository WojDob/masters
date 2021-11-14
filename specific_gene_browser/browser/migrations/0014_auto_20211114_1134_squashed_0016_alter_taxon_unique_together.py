# Generated by Django 3.2.5 on 2021-11-14 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('browser', '0014_auto_20211114_1134'), ('browser', '0015_alter_taxon_name'), ('browser', '0016_alter_taxon_unique_together')]

    dependencies = [
        ('browser', '0013_auto_20211107_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxon',
            options={},
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='accession',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='family',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='genus',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='genus_isolation_index',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='protein_count',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='species_isolation_index',
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('protein_count', models.PositiveIntegerField(blank=True, null=True)),
                ('species_isolation_index', models.FloatField(blank=True, null=True)),
                ('genus_isolation_index', models.FloatField(blank=True, null=True)),
                ('lineage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.lineage')),
            ],
        ),
        migrations.AlterField(
            model_name='taxon',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterUniqueTogether(
            name='taxon',
            unique_together={('name', 'taxonomic_unit')},
        ),
    ]
