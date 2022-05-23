
import json
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from app1.models import *
from app1.serialiser import *
# Create your views here.

def home(request):
    return HttpResponse("All Working Fine..")

def about(request):
    return HttpResponse("This API is created By Keshav Jha")

def BornesHorsRue(request):
    if request.method=='GET':
        data=list(BornesHorsRueDB.objects.values())
        
        return JsonResponse(data, safe=False)
    return HttpResponse("NOT A REQUEST")


def fetchdata(request,password="none",db="BH",count=None,initial=None,final=None):
    print(count)
    try:

        if password=="keshavjha":
            if  db =="BH":
                db=BornesHorsRueDB
            elif db=="BS":
                db=BornesSurRueDB
            elif db=="DE":
                db=DateExportationDB
            elif db=="ER":
                db=EmplacementReglementationBD
            elif db=="PR":
                db=PeriodesDB
            elif db=="PC":
                db=PlacesDB
            elif db=="RP":
                db=ReglementationPeriodeDB
            elif db=="RL":
                db=ReglementationsDB

            else:
                db=BornesHorsRueDB
            
            # userobject=database.objects.all()
            if ((count==None) and (initial==None) and (final==None)):
                data=list(db.objects.values())



            elif count:
                try:
                    data=list(db.objects.values()[:int(count)])
                except:
                    
                    return HttpResponse("No Data Found ;)")


            elif ( initial == None) and (final == None ):
                data=list(db.objects.values())
                

            elif (initial and final):
                try:
                    data=list(db.objects.values()[int(initial)-1:int(final)])
                except:
                    return HttpResponse("No Data Found")

            # serialisedObject=BornesHorsRueAPI(userobject,many=True)

            # jsonFormat=json.dumps(serialisedObject.data)
            # return JsonResponse(serialisedObject.data,safe=False)
            # return JsonResponse(json.loads(jsonFormat),safe=False)
            if len(data)==0:
                return HttpResponse("No Data Found")
            else:    
                return JsonResponse(data, safe=False)

        else:
            return HttpResponse("You are not authorised")
    
    except:
        return HttpResponse("Something Went Wrong ;) Try Contacting Keshav")