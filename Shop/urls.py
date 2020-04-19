from django.urls import path
from Shop import views
app_name='shop'

urlpatterns = [
    path('',views.index,name="index"),
    path('donation/',views.donation,name='donation'),
    path('shop/',views.shop,name='shop'),
    path('shop/register/',views.registerShop,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('userregister/',views.UserReistration,name='userregister'),
    path('shopadmin/',views.shopadmin,name='shopadmin')
]
