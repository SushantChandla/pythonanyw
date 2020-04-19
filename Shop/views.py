from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm,ShopForm
from .models import ShopRegistration,orders
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from django.http import Http404 



# Create your views here.
def index(request):
    return render(request,'Shop/landingp.html')


def donation(request):
    return render(request,'Shop/donation.html')

def checkfilter(a,address):
    return a in address

def shop(request):
    if request.method == 'POST':
        if request.POST.get("q")!=None:
            data=ShopRegistration.objects.filter(address__contains=request.POST.get("q"))
            return render(request,'Shop/shop.html',{'shops':data,'orderplaced':False})
        usernameg=request.POST.get('username')
        order_detailsg=request.POST.get('order')
        phone_numberg=request.POST.get('userContact')
        addressg=request.POST.get('userAddress')
        shopnumber=request.POST.get('shopnumber')
        print(order_detailsg)
        if len(ShopRegistration.objects.all().filter(phone_number=shopnumber))==1:
            orders.objects.get_or_create(shop=ShopRegistration.objects.all().get(phone_number=shopnumber),
            username=usernameg ,  order_details=order_detailsg , address=addressg , phone_number=phone_numberg)
            data=ShopRegistration.objects.all()
            return render(request,'Shop/shop.html',{'shops':data,'orderplaced':True})
       
    else:
        data=ShopRegistration.objects.all()
        return render(request,'Shop/shop.html',{'shops':data,'orderplaced':False})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')



def UserReistration(request):
    if request.user.is_authenticated:
        raise Http404
    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        user_form=UserForm()
        return render(request,'accounts/userregistration.html',
                        {'user_form':user_form,'login':True})


def registerShop(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        shop_form = ShopForm(data=request.POST)
        if user_form.is_valid() and shop_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            shop = shop_form.save(commit=False)

            shop.user = user
            shop.shop_pic = request.FILES['shop_pic']

            shop.save()
            registered = True

            return redirect('/')

        else:
            print(user_form.errors,shop_form.errors)

    else:
        user_form = UserForm()
        shop_form = ShopForm()

    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'shop_form':shop_form,
                           'registered':registered
                           ,'login':True})

    

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return redirect('/')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'accounts/login.html', {'login':True})

@login_required
def shopadmin(request):
    if len(ShopRegistration.objects.filter(user=request.user))==1:
        return render(request,'Shop/shopadmin.html',{'orders':orders.objects.filter(shop=ShopRegistration.objects.get(user=request.user)),'shop':ShopRegistration.objects.get(user=request.user)})
    else:
        raise Http404

