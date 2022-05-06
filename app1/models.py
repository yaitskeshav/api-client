from ast import mod
from django.db import models

# Create your models here.

class BornesHorsRueDB(models.Model):
    nNoBorne=models.IntegerField()
    sTerrain=models.CharField(max_length=20)
    sNomRuePrincipale=models.CharField(max_length=200)
    sStatut=models.CharField(max_length=2)
    nLongitude=models.FloatField()
    nLatitude=models.FloatField()
    Lun=models.BooleanField()
    Mar=models.BooleanField()	
    Mer=models.BooleanField()	
    Jeu=models.BooleanField()	
    Ven=models.BooleanField()	
    Sam=models.BooleanField()	
    Dim=models.BooleanField()	
    dtHeureDebutAP=models.TimeField()	
    dtHeureFinAP=models.TimeField()
    nTarifHoraire=models.IntegerField()
    nMax=models.IntegerField()

    def __str__(self):
        return self.sTerrain



class BornesSurRue(models.Model):
    pass


class DateExportation(models.Model):
    pass


class EmplacementReglementation(models.Model):
    pass

class Periodes(models.Model):
    pass

class Places(models.Model):
    pass



class ReglementationPeriode(models.Model):
    pass


class Reglementations(models.Model):
    pass



