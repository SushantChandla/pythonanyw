from django.urls import path
from Map import views

app_name= 'map'

urlpatterns = [
    path('',views.index,name="Home"),
]
