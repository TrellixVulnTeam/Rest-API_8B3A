from rest_framework.serializers import Serializer
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from App1.models import Car
from App1.serializers import CarSerializer

class Detail_View(APIView):

    def get(self, request):

        cars = Car.objects.all()
        serializer = CarSerializer(cars, many = True)

        return Response(serializer.data, status.HTTP_200_OK) 

    def post(self, request):

        serializer = CarSerializer(data = request.data)
     
        if serializer.is_valid():
     
            serializer.save()
     
            return Response(serializer.data, status= status.HTTP_201_CREATED)
     
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
    
    
    
class Update_View(APIView):
   
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarSerializer(snippet)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Using Mixins

from App1.models import Car
from App1.serializers import CarSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

class CarList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

 #Using Generics

from rest_framework import generics
from App1.models import Car
from App1.serializers import CarSerializer
from App1.permissions import IsOwnerOrReadOnly

class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                     IsOwnerOrReadOnly]
from django.contrib.auth.models import User
from App1.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    