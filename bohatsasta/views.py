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

class FlightView(viewsets.ModelViewSet):
    serializer_class = FlightSerializers
    queryset = Flight.objects.all()



class userView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class DetailView(viewsets.ModelViewSet):
    serializer_class = DetailsSerializers
    queryset = Details.objects.all()

class CardList(APIView):
    # permission_classes = [IsAuthenticated] 

    def get(self,request):
        card = Card.objects.all()
        card_serializers = CardSerializers(card,many=True)
        # return JsonResponse(card_serializers.data,safe=False)
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

    


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializers
    queryset = Ticket.objects.all()

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
#  class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)


class HelloView(APIView):
    permission_classes = [IsAuthenticated]            # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


