from django.shortcuts import render
from Map.models import Infected
import requests

# Create your views here.

def index(request):
    dic={'data':Infected.objects.all()}
    return render(request,'Map/map.html',context=dic)