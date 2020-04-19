from django.db import models

# Create your models here.

class Infected (models.Model):
    State=models.CharField(max_length=255,default="India");
    District=models.CharField(max_length=255,default="");
    lan=models.FloatField();
    lat=models.FloatField();
    corona=models.IntegerField(default=0);
    death=models.IntegerField(default=0);
    
    def __str__(self):
        return 'State {state} District {district} lan {lan} lat {lat} Infected {Corona} Death {death}'.format(
            district=self.District,state=self.State,lan=self.lan,lat=self.lat,Corona=self.corona,death=self.death)


