
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from app1.models import *
from app1.serialiser import *
# Create your views here.

def home(request):
    return HttpResponse("All Working Fine..")



def BornesHorsRue(request):

    data=list(BornesHorsRueDB.objects.values())
    print("printing type of data ////" , type(data))
    return JsonResponse(data, safe=False)

def fetchdata(request,password="none",db="BH",):
    if password=="keshavjha":
        if   db =="BH":
            database=BornesHorsRueDB
        elif db=="BS":
            database=BornesSurRueDB
        elif db=="DE":
            database=DateExportationDB
        elif db=="ER":
            database=EmplacementReglementationBD
        elif db=="PR":
            database=PeriodesDB
        elif db=="PC":
            database=PlacesDB
        elif db=="RP":
            database=ReglementationPeriodeDB
        elif db=="RL":
            database=ReglementationsDB

        # userobject=database.objects.all()
        data=list(database.objects.values())
        # serialisedObject=BornesHorsRueAPI(userobject,many=True)

        # jsonFormat=json.dumps(serialisedObject.data)
        # return JsonResponse(serialisedObject.data,safe=False)
        # return JsonResponse(json.loads(jsonFormat),safe=False)

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("You are not authorised")