from ast import mod
from django.db import models

# Create your models here.

class BornesHorsRueDB(models.Model):
    nNoBorne            =models.IntegerField()
    sTerrain            =models.CharField(max_length=20)
    sNomRuePrincipale   =models.CharField(max_length=200)
    sStatut             =models.CharField(max_length=2)
    nLongitude          =models.FloatField()
    nLatitude           =models.FloatField()
    Lun                 =models.BooleanField()
    Mar                 =models.BooleanField()	
    Mer                 =models.BooleanField()	
    Jeu                 =models.BooleanField()	
    Ven                 =models.BooleanField()	
    Sam                 =models.BooleanField()	
    Dim                 =models.BooleanField()	
    dtHeureDebutAP      =models.TimeField()	
    dtHeureFinAP        =models.TimeField()
    nTarifHoraire       =models.IntegerField()
    nMax                =models.IntegerField()





class BornesSurRueDB(models.Model):
    nNoBorne            =models.IntegerField(blank=True)
    sStatut             =models.CharField(max_length=2,blank=True)
    sNomRue             =models.CharField(max_length=200,blank=True)
    sZoneGroupeCode	    =models.CharField(max_length=100,blank=True)
    nLongitude	        =models.FloatField(blank=True)
    nLatitude           =models.FloatField(blank=True)
    sTypeExploitation   =models.CharField(max_length=200,blank=True)



class DateExportationDB(models.Model):
    dDate               =models.DateField(blank=True)



class EmplacementReglementationBD(models.Model):
    sNoEmplacement  	= models.CharField(max_length=100,blank=True)
    sCodeAutocollant    = models.CharField(max_length=100,blank=True)


class PeriodesDB(models.Model):
    nID	         = models.IntegerField(blank=True)
    dtHeureDebut = models.TimeField(blank=True)		
    dtHeureFin	 = models.TimeField(blank=True)	
    bLun	     = models.IntegerField(blank=True)
    bMar	     = models.IntegerField(blank=True)
    bMer	     = models.IntegerField(blank=True)
    bJeu	     = models.IntegerField(blank=True)
    bVen	     = models.IntegerField(blank=True)
    bSam	     = models.IntegerField(blank=True)
    bDim         = models.IntegerField(blank=True)


class PlacesDB(models.Model):
    sNoPlace	                = models.CharField( max_length=200,blank=True)
    nLongitude	                = models.FloatField(blank=True)
    nLatitude	                = models.FloatField(blank=True)
    nPositionCentreLongitude	= models.FloatField(blank=True)
    nPositionCentreLatitude	    = models.FloatField(blank=True)
    sStatut	                    = models.IntegerField(blank=True)
    sGenre	                    = models.CharField( max_length=200,blank=True)
    sType	                    = models.CharField( max_length=200, blank=True)
    sAutreTete	                = models.CharField( max_length=200, blank=True,null=True)
    sNomRue	                    = models.CharField(max_length=250,blank=True)
    nSupVelo	                = models.IntegerField(blank=True)
    sTypeExploitation	        = models.CharField( max_length=200, blank=True)
    nTarifHoraire	            = models.IntegerField()
    sLocalisation	            = models.CharField( max_length=2, blank=True)
    nTarifMax                   = models.CharField( max_length=200, blank=True,null=True,default=None)

    def __str__(self):
        return self.sNoPlace


class ReglementationPeriodeDB(models.Model):
    sCode	      =    models.CharField( max_length=100,blank=True)
    noPeriode	  =    models.IntegerField(blank=True)
    sDescription  =    models.CharField(max_length=250,blank=True)



class ReglementationsDB(models.Model):
    Name          =    models.CharField( max_length=50,blank=True)	
    Type	      =    models.CharField( max_length=50,blank=True)	
    DateDebut	  =    models.IntegerField(blank=True)
    DateFin	      =    models.IntegerField(blank=True)
    maxHeures     =    models.IntegerField(blank=True)




