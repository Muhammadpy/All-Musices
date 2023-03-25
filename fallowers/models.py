from ast import mod
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fallower(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Ismi", unique=True, max_length=55,blank=True)
    surname = models.CharField(max_length=55)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    adress = models.CharField(max_length=500)
    
    # models.PositiveIntegerField(default=0)
    # models.ImageField()
    # models.ForeignKey()
    # models.ManyToManyField()    
    # models.OneToOneField()
    # models.TextField()
    # models.TimeField()
    # models.DateField()
    # models.DateTimeField()
    # models.SlugField()
    # models.BooleanField()
    
    # models.DurationField() 
    # models.AutoField() 
    # models.FloatField() 
    # models. URLField() 
    # models.NullBooleanField()
    # models.UUIDField()
    # models.IntegerField()
    # models.BigIntegerField()
    # models.SmallIntegerField()
    # models.SmallPositiveIntegerField(default=0)
    # models.BigPositiveIntegerField(default=0)
