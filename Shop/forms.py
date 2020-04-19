from django import forms
from django.contrib.auth.models import User
from .models import ShopRegistration

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class ShopForm(forms.ModelForm):
    class Meta():
        model = ShopRegistration
        fields = ('address','shop_pic','phone_number')
