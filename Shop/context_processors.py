from .models import ShopRegistration

def checkforshopkeper(request):
    shopkeper=False
    if request.user.is_authenticated:   
        if len(ShopRegistration.objects.filter(user=request.user))==1:
            shopkeper=True
    return {'shopkeper':shopkeper}