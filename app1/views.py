
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from app1.models import *
# Create your views here.

def home(request):
    return HttpResponse("All Working Fine..")



def BornesHorsRue(request):

    data=list(BornesHorsRueDB.objects.values())
    print("printing type of data ////" , type(data))
    return JsonResponse(data, safe=False)
