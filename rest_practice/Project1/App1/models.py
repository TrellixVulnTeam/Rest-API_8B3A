from django.db import models
from django.db.models.deletion import CASCADE


class Car(models.Model):

    c_name = models.CharField(max_length=50) 
    c_color = models.CharField(max_length=10)
    manufacture_year = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=50)   
    owner = models.ForeignKey('auth.User', related_name='Cars', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
    
     super(Car, self).save(*args, **kwargs)