from django.db import models
from django.contrib.auth.models import User



class ShopRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256,blank=False)
    shop_pic = models.ImageField(upload_to='shopimage',blank=False)
    phone_number=models.CharField(max_length=10)
    def __str__(self):
        return self.user.username


class orders(models.Model):
    username=models.CharField(max_length=256,blank=False)
    order_details=models.TextField()
    address=models.CharField(max_length=256,blank=False)
    phone_number=models.CharField(max_length=10)
    shop=models.ForeignKey('ShopRegistration', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return 'username: {u} order:{o}'.format(u=self.username,o=self.order_details)