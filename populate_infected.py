import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CoronaWeb.settings')
import django
django.setup()
from Map.models  import Infected 
import requests
from Shop.models import orders



def populate():
    data=requests.get("https://api.covid19india.org/v2/state_district_wise.json")
    data=data.json()
    for nstate in data:
        for district in nstate['districtData']:
            state=nstate['state']
            Dis=district['district']
            cor=district['confirmed']
            dead=district['delta']['confirmed']
            if(Dis=="Unknown"):
                Dis=""
            loglat = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/"+state+"%20"+Dis
                                    +".json?access_token=pk.eyJ1IjoibmlzaGFudC1jaGFuZGxhIiwiYSI6ImNrOGs4eWw3djBrbjEzZHFob3hiOHp1bDgifQ.l4Vjz4vaAKos0VKLAEDKxg")
            if(len(loglat.json()['features'])>0):    
                loglat=loglat.json()['features'][0]['center']
                if Infected.objects.filter(lan=loglat[0],lat=loglat[1]).exists():
                    entry=Infected.objects.get(lan=loglat[0],lat=loglat[1])
                    entry.corona+=cor
                    entry.death+=dead
                    entry.save(update_fields=['corona','death'])
                else:
                    Infected.objects.get_or_create(State=state,District=Dis,lan=loglat[0],lat=loglat[1],corona=cor,death=dead)
    
def clear():
    orders.objects.all().delete()

if __name__ == "__main__":
    # Infected.objects.all().delete()
    # populate()
    clear()
    print("DONE")