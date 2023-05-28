from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Event Name', max_length=120)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=120)
    phone = models.CharField(max_length=120,blank=True)
    web = models.URLField('Website Address',blank=True)
    email = models.EmailField('Email Address',blank=True)
    owner = models.IntegerField(default=1, blank=False)
    def __str__(self):
        return self.name
    
class MyClubeUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue,on_delete= models.CASCADE,blank=True, null=True)
    manager = models.ForeignKey(User,on_delete= models.SET_NULL,null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    participats = models.ManyToManyField(MyClubeUser,blank=True)
    
    def __str__(self):
        return self.name

