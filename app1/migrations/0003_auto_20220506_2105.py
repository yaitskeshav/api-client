# Generated by Django 3.2.6 on 2022-05-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_borneshorsrue_borneshorsruedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='BornesSurRueDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nNoBorne', models.IntegerField(blank=True)),
                ('sStatut', models.CharField(blank=True, max_length=2)),
                ('sNomRue', models.CharField(blank=True, max_length=200)),
                ('sZoneGroupeCode', models.CharField(blank=True, max_length=100)),
                ('nLongitude', models.FloatField(blank=True)),
                ('nLatitude', models.FloatField(blank=True)),
                ('sTypeExploitation', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DateExportationDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dDate', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmplacementReglementationBD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sNoEmplacement', models.CharField(blank=True, max_length=100)),
                ('sCodeAutocollant', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nID', models.IntegerField(blank=True)),
                ('dtHeureDebut', models.TimeField(blank=True)),
                ('dtHeureFin', models.TimeField(blank=True)),
                ('bLun', models.IntegerField(blank=True)),
                ('bMar', models.IntegerField(blank=True)),
                ('bMer', models.IntegerField(blank=True)),
                ('bJeu', models.IntegerField(blank=True)),
                ('bVen', models.IntegerField(blank=True)),
                ('bSam', models.IntegerField(blank=True)),
                ('bDim', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlacesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sNoPlace', models.CharField(blank=True, max_length=50)),
                ('nLongitude', models.FloatField(blank=True)),
                ('nLatitude', models.FloatField(blank=True)),
                ('nPositionCentreLongitude', models.FloatField(blank=True)),
                ('nPositionCentreLatitude', models.FloatField(blank=True)),
                ('sStatut', models.IntegerField(blank=True)),
                ('sGenre', models.CharField(blank=True, max_length=200)),
                ('sType', models.CharField(blank=True, max_length=200)),
                ('sAutreTete', models.CharField(blank=True, max_length=200)),
                ('sNomRue', models.CharField(blank=True, max_length=250)),
                ('nSupVelo', models.IntegerField(blank=True)),
                ('sTypeExploitation', models.CharField(blank=True, max_length=200)),
                ('nTarifHoraire', models.IntegerField()),
                ('sLocalisation', models.CharField(blank=True, max_length=2)),
                ('nTarifMax', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReglementationPeriodeDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sCode', models.CharField(blank=True, max_length=100)),
                ('noPeriode', models.IntegerField(blank=True)),
                ('sDescription', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ReglementationsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Type', models.CharField(blank=True, max_length=50)),
                ('DateDebut', models.IntegerField(blank=True)),
                ('DateFin', models.IntegerField(blank=True)),
                ('maxHeures', models.IntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BornesSurRue',
        ),
        migrations.DeleteModel(
            name='DateExportation',
        ),
        migrations.DeleteModel(
            name='EmplacementReglementation',
        ),
        migrations.DeleteModel(
            name='Periodes',
        ),
        migrations.DeleteModel(
            name='Places',
        ),
        migrations.DeleteModel(
            name='ReglementationPeriode',
        ),
        migrations.DeleteModel(
            name='Reglementations',
        ),
    ]
