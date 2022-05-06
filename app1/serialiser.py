from rest_framework import serializers



class BornesHorsRueAPI(serializers.Serializer):
    nNoBorne=serializers.IntegerField()
    sTerrain=serializers.CharField(max_length=20)
    sNomRuePrincipale=serializers.CharField(max_length=200)
    sStatut=serializers.CharField(max_length=2)
    nLongitude=serializers.FloatField()
    nLatitude=serializers.FloatField()
    Lun=serializers.BooleanField()
    Mar=serializers.BooleanField()	
    Mer=serializers.BooleanField()	
    Jeu=serializers.BooleanField()	
    Ven=serializers.BooleanField()	
    Sam=serializers.BooleanField()	
    Dim=serializers.BooleanField()	
    dtHeureDebutAP=serializers.TimeField()	
    dtHeureFinAP=serializers.TimeField()
    nTarifHoraire=serializers.IntegerField()
    nMax=serializers.IntegerField()


