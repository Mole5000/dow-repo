from django.db import models


# Create your models here.

class CommonInfo(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(blank=True)
    history = models.TextField(blank=True)
    
    class Meta:
        abstract = True
    
class Player(models.Model):
    name =  models.CharField(max_length=50)
    points = models.IntegerField()
    points_bonus = models.IntegerField()
    turn_order = models.IntegerField()

class Race(CommonInfo):
    alignment = models.IntegerField()
    sub_race = models.ForeignKey("self",blank=True,null=True)

class City(CommonInfo):
    race = models.ForeignKey(Race)
    alignment = models.IntegerField()

class RaceAdvancement(models.Model):
    label = models.CharField(max_length=50)
    race = models.ForeignKey(Race)

class CityAdvancement(models.Model):
    label = models.CharField(max_length=50)
    city = models.ForeignKey(City)

class Avatar(CommonInfo):
    owner = models.ForeignKey(Player)
    created_race = models.ForeignKey(Race,blank=True,null=True)

class Order(CommonInfo):
    owner = models.ForeignKey(Player)
    race = models.ForeignKey(Race)
    religious = models.BooleanField()

class History(models.Model):
    turn_by = models.ForeignKey(Player)
    turn_number = models.IntegerField()
    description = models.TextField()