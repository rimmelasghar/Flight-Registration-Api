from pyexpat import model
from zoneinfo import available_timezones
from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    name = models.CharField(max_length=30)
    num = models.CharField(max_length=30,unique=True)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.CharField(max_length=30)
    seats  = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.num
    
class Details(models.Model):
    flight = models.ForeignKey(Flight,related_name='details',on_delete = models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    available_seats = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.flight.num

    
class Card(models.Model):
    number = models.CharField(max_length=30)
    choices = [
        ('mc',"MASTER CARD"),
        ('vc',"VISA CARD")
    ]
    card_type = models.CharField(choices=choices,max_length=3)
    profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name='card')

    def __str__(self):
        return self.number

class Ticket(models.Model):
    profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name='ticket')
    details = models.ForeignKey(Details,on_delete = models.CASCADE)
    ticketid = models.AutoField(primary_key=True)
    choices = [
        ('A',"Active"),
        ('NA',"Non-Active")
    ]
    status = models.CharField(choices=choices,max_length=30)
