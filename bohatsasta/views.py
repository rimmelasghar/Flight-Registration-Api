from ast import Delete
import json
from urllib import request, response
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import UserSerializer,FlightSerializers,DetailsSerializers,CardSerializers,TicketSerializers,RegisterSerializer
from .models import Flight,Ticket,Details,Card
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from bohatsasta import serializers
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication




class FlightView(viewsets.ModelViewSet):
    serializer_class = FlightSerializers
    queryset = Flight.objects.all()


class DetailView(viewsets.ModelViewSet):
    serializer_class = DetailsSerializers
    queryset = Details.objects.all()

####
### Card - Views
####

class CardList(APIView):
    # permission_classes = [IsAuthenticated] 

    def get(self,request):
        card = Card.objects.all()
        card_serializers = CardSerializers(card,many=True)
        return Response(card_serializers.data)
    def post(self,request,format = None):
        card_serializers = CardSerializers(data = request.data)
        if card_serializers.is_valid():
            card_serializers.save()
            return Response(card_serializers.data,status=status.HTTP_201_CREATED)
        return Response(card_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CardCRUD(APIView):
    # List all snippets, or create a new snippet.
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        card_serializer = CardSerializers(card)
        return Response(card_serializer.data)
    # permission_classes = [IsAuthenticated] 
    def put(self,request,pk,format = None):
        card = self.get_object(pk)
        card_serializers = CardSerializers(card,data = request.data)
        if card_serializers.is_valid():
            card_serializers.save()
            return Response(card_serializers.data)
        return Response(card_serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format = None):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


class TicketView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        ticket = Ticket.objects.filter(profile = user)
        ticket_serializers = TicketSerializers(ticket,many=True)
        print(ticket_serializers.data)
        return Response(ticket_serializers.data)
    def post(self,request,format = None):
        ticket_serializers = TicketSerializers(data = request.data)
        if ticket_serializers.is_valid():
            ticket_serializers.save()
            return Response(ticket_serializers.data,status=status.HTTP_201_CREATED)
        return Response(ticket_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

####
### USER - Views
####
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class HelloView(APIView):
    permission_classes = [IsAuthenticated]            # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


