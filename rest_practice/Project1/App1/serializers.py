from re import I
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from App1.models import Car


class CarSerializer(ModelSerializer):


    class Meta:

        model = Car
        fields = ['c_name','c_color','manufacture_year','manufacturer']

        def create(self, validated_data):
            return Car.create(validated_data)    

        def update(self, instance, validated_data ):
            instance.c_name = validated_data.get('c_name', instance.c_name)
            instance.c_color = validated_data.get('c_color', instance.c_color)
            instance.manufacture_year = validated_data.get('manufacture_year', instance.manufacture_year)
            instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
            instance.save()
            return instance

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer)   :
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())


    class Meta:
        model = User
        fields = ['id', 'username', 'cars']                