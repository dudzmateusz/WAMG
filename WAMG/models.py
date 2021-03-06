import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings


class contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.email



class things(models.Model):
    def upload_path(instance, filename):
        return 'images/%s/%s' % (instance.user, filename)

    TYPE_LIST = [('1','๐ - Car'),
                 ('2','๐  - Room'),
                 ('3','๐ง - Garage'),
                 ('4','๐ - Garden'),
                 ('5','๐ - Basement'),
                 ('6','๐งน - Terrace'),
                 ('7','๐ป - Attic'),
                 ('8','๐ - Bathroom'),
                 ('9','๐ฝ๏ธ - Kitchen'),
                 ('10','๐ด - Barn'),
                 ('11','๐ - Semitrailer'),
                 ('12','๐ง - Owned by Friend'),
                 ('13','๐ช - Owned by Family'),
                 ('14','โบ - Summer house'),
                 ('15','โ - Other')]

    COLOR_LIST = [('1', '๐ด'),
                 ('2', '๐ '),
                 ('3', '๐ก'),
                 ('4', '๐ข'),
                 ('5', '๐ต'),
                 ('6', '๐ฃ'),
                 ('7', '๐ค'),
                 ('8', 'โซ'),
                 ('9', 'โช'),
                 ]
    name = models.CharField(max_length=100,help_text ="Put name from your thing")
    sku = models.CharField(max_length=30,help_text = "Put sku your thing",default='-')
    ean = models.CharField(max_length=30,help_text = "Put ean your thing",blank=True,default='-')
    color = models.CharField(max_length=30, choices=COLOR_LIST, default='-',blank=True)
    note = models.CharField(max_length=200,help_text ="You can describe your thing here...",blank=True,default='-')
    date_add = models.DateField(auto_now=False, auto_now_add=False)
    place = models.CharField(max_length=30, choices=TYPE_LIST, default='2')
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=upload_path, blank=True, null=True)


    def __str__(self):
        return self.user


