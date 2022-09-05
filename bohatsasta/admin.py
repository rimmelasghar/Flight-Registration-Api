from django.contrib import admin

# Register your models here.
from .models import Flight,Details,Ticket,Card

admin.site.register(Flight)
admin.site.register(Details)
admin.site.register(Ticket)
admin.site.register(Card)